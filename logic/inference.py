# ===================================
# ENGINE SỬ LUẬN LOGIC FORWARD CHAINING
# ===================================
# Sử dụng Forward Chaining (suy luận tiến)
# để áp dụng các quy tắc và suy ra các sự kiện mới

from typing import Set, List, Dict, Optional
from .rules import KnowledgeBase, Predicate, Rule


def match_predicate(condition: Predicate, fact: Predicate, binding: Dict[str, str]) -> Optional[Dict[str, str]]:
    """Thử ghép một điều kiện với một fact, trả về binding nếu phù hợp."""
    if condition.name != fact.name or len(condition.args) != len(fact.args):
        return None
    binding = dict(binding)
    for arg, value in zip(condition.args, fact.args):
        if Predicate.is_variable(arg):
            if arg in binding:
                if binding[arg] != value:
                    return None
            else:
                binding[arg] = value
        elif arg != value:
            return None
    return binding


class LogicInferenceEngine:
    """Engine suy luận logic sử dụng Forward Chaining"""
    
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        self.inferred_facts: Set[Predicate] = set()  # Sự kiện được suy ra
        self.applied_rules: List[str] = []  # Danh sách quy tắc đã áp dụng
        self.applied_bindings: Set[tuple] = set()
    
    def get_all_facts(self) -> Set[Predicate]:
        """Lấy tất cả sự kiện (gốc + suy ra)"""
        return self.kb.facts | self.inferred_facts
    
    def find_bindings(self, rule: Rule) -> List[Dict[str, str]]:
        """Tìm tất cả các binding thỏa mãn điều kiện của một quy tắc."""
        bindings: List[Dict[str, str]] = [{}]
        all_facts = self.get_all_facts()
        
        for condition in rule.conditions:
            next_bindings: List[Dict[str, str]] = []
            for binding in bindings:
                for fact in all_facts:
                    new_binding = match_predicate(condition, fact, binding)
                    if new_binding is not None:
                        next_bindings.append(new_binding)
            bindings = next_bindings
            if not bindings:
                break
        return bindings
    
    def can_apply_rule(self, rule: Rule) -> bool:
        """Kiểm tra xem quy tắc có thể áp dụng được không."""
        bindings = self.find_bindings(rule)
        for binding in bindings:
            substituted = [conclusion.substitute(binding) for conclusion in rule.conclusions]
            if any(conclusion not in self.get_all_facts() for conclusion in substituted):
                return True
        return False
    
    def apply_rule(self, rule: Rule):
        """Áp dụng quy tắc: thêm tất cả kết luận vào sự kiện suy ra"""
        bindings = self.find_bindings(rule)
        for binding in bindings:
            binding_key = (rule.name, tuple(sorted(binding.items())))
            if binding_key in self.applied_bindings:
                continue
            self.applied_bindings.add(binding_key)

            for conclusion in rule.conclusions:
                substituted = conclusion.substitute(binding)
                self.inferred_facts.add(substituted)
            self.applied_rules.append(rule.name)
    
    def forward_chain(self, max_iterations: int = 10) -> Set[Predicate]:
        """
        Thực hiện Forward Chaining:
        Liên tục áp dụng các quy tắc cho đến khi không có quy tắc nào có thể áp dụng thêm
        
        Args:
            max_iterations: Số lần lặp tối đa (để tránh vòng lặp vô hạn)
        
        Returns:
            Tập hợp tất cả sự kiện (ban đầu + suy ra)
        """
        # Sắp xếp quy tắc theo độ ưu tiên (cao hơn = thực thi trước)
        sorted_rules = sorted(self.kb.rules, key=lambda r: r.priority, reverse=True)
        
        iteration = 0
        changed = True
        
        while changed and iteration < max_iterations:
            changed = False
            iteration += 1
            
            for rule in sorted_rules:
                if self.can_apply_rule(rule):
                    before_count = len(self.inferred_facts)
                    self.apply_rule(rule)
                    after_count = len(self.inferred_facts)
                    
                    if after_count > before_count:
                        changed = True
                        print(f"[Lan lap {iteration}] Ap dung quy tac: {rule.name}")
                        print(f"  -> Ket luan: {[str(c) for c in rule.conclusions]}")
        
        return self.get_all_facts()
    
    def get_applied_rules(self) -> List[str]:
        """Lấy danh sách các quy tắc đã áp dụng"""
        return self.applied_rules
    
    def explain_conclusion(self, predicate: Predicate) -> str:
        """Giải thích tại sao một sự kiện được suy ra"""
        if self.kb.has_fact(predicate):
            return f"✓ {predicate} la su kien goc (ton tai tu ban dau)"
        
        if predicate in self.inferred_facts:
            for rule in self.kb.rules:
                for binding in self.find_bindings(rule):
                    for conclusion in rule.conclusions:
                        inferred = conclusion.substitute(binding)
                        if inferred == predicate:
                            conditions_str = " ∧ ".join(str(cond.substitute(binding)) for cond in rule.conditions)
                            return f"✓ {predicate} duoc suy ra boi quy tac '{rule.name}': {conditions_str} -> {predicate}"
        
        return f"✗ {predicate} khong duoc suy ra"


def run_inference(kb: KnowledgeBase) -> None:
    """Chạy engine suy luận và hiển thị kết quả"""
    print("=" * 60)
    print("ENGINE SUY LUAN LOGIC - FORWARD CHAINING")
    print("=" * 60)
    
    print("\n[1] SU KIEN BAN DAU (Facts):")
    for fact in sorted(kb.facts, key=lambda f: f.name):
        print(f"  - {fact}")
    
    print(f"\n[2] SO QUY TAC: {len(kb.rules)}")
    for rule in sorted(kb.rules, key=lambda r: r.priority, reverse=True):
        print(f"  - {rule}")
    
    # Thực hiện suy luận
    engine = LogicInferenceEngine(kb)
    all_facts = engine.forward_chain()
    
    print(f"\n[3] KET QUA SAU SUY LUAN:")
    print(f"  - Tong su kien: {len(all_facts)}")
    print(f"  - Quy tac ap dung: {len(engine.get_applied_rules())}")
    
    print(f"\n[4] DANH SACH TAT CA SU KIEN:")
    for fact in sorted(all_facts, key=lambda f: f.name):
        status = "SUY RA" if fact in engine.inferred_facts else "GOC"
        print(f"  {status} | {fact}")
        explanation = engine.explain_conclusion(fact)
        if "SUY RA" in explanation:
            print(f"       {explanation}")
    
    print(f"\n[5] HANH DONG TU DONG HOA:")
    # Tìm tất cả hành động (action predicates)
    actions = {fact for fact in all_facts if any(
        name in fact.name for name in ["light_on", "light_off", "ac_on", "door_locked", "energy_saving"]
    )}
    if actions:
        for action in sorted(actions, key=lambda a: a.name):
            print(f"  HANH DONG: {action}")
    else:
        print("  (Khong co hanh dong tu dong hoa)")
    
    print("\n" + "=" * 60)
