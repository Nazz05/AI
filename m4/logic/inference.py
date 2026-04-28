# ===================================
# ENGINE SỬ LUẬN LOGIC FORWARD CHAINING
# ===================================
# Sử dụng Forward Chaining (suy luận tiến)
# để áp dụng các quy tắc và suy ra các sự kiện mới

from typing import Set, List
from .rules import KnowledgeBase, Predicate, Rule


class LogicInferenceEngine:
    """Engine suy luận logic sử dụng Forward Chaining"""
    
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        self.inferred_facts: Set[Predicate] = set()  # Sự kiện được suy ra
        self.applied_rules: List[str] = []  # Danh sách quy tắc đã áp dụng
    
    def matches_condition(self, condition: Predicate) -> bool:
        """Kiểm tra xem điều kiện có được thỏa mãn không
        (sự kiện đó tồn tại trong cơ sở kiến thức)
        """
        return self.kb.has_fact(condition) or condition in self.inferred_facts
    
    def can_apply_rule(self, rule: Rule) -> bool:
        """Kiểm tra xem tất cả điều kiện của quy tắc có được thỏa mãn không"""
        return all(self.matches_condition(cond) for cond in rule.conditions)
    
    def apply_rule(self, rule: Rule):
        """Áp dụng quy tắc: thêm tất cả kết luận vào sự kiện suy ra"""
        for conclusion in rule.conclusions:
            self.inferred_facts.add(conclusion)
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
                    # Kiểm tra xem quy tắc chưa được áp dụng
                    before_count = len(self.inferred_facts)
                    self.apply_rule(rule)
                    after_count = len(self.inferred_facts)
                    
                    if after_count > before_count:
                        changed = True
                        print(f"[Iteration {iteration}] Applied rule: {rule.name}")
                        print(f"  → Conclusions: {[str(c) for c in rule.conclusions]}")
        
        # Kết hợp sự kiện gốc + sự kiện suy ra
        all_facts = self.kb.facts | self.inferred_facts
        return all_facts
    
    def get_all_facts(self) -> Set[Predicate]:
        """Lấy tất cả sự kiện (gốc + suy ra)"""
        return self.kb.facts | self.inferred_facts
    
    def get_applied_rules(self) -> List[str]:
        """Lấy danh sách các quy tắc đã áp dụng"""
        return self.applied_rules
    
    def explain_conclusion(self, predicate: Predicate) -> str:
        """Giải thích tại sao một sự kiện được suy ra"""
        if self.kb.has_fact(predicate):
            return f"✓ {predicate} là sự kiện gốc (tồn tại từ ban đầu)"
        
        if predicate in self.inferred_facts:
            # Tìm quy tắc nào suy ra sự kiện này
            for rule in self.kb.rules:
                if predicate in rule.conclusions and self.can_apply_rule(rule):
                    conditions_str = " ∧ ".join(str(c) for c in rule.conditions)
                    return f"✓ {predicate} được suy ra bởi quy tắc '{rule.name}': {conditions_str} → {predicate}"
        
        return f"✗ {predicate} không được suy ra"


def run_inference(kb: KnowledgeBase) -> None:
    """Chạy engine suy luận và hiển thị kết quả"""
    print("=" * 60)
    print("LOGIC INFERENCE ENGINE - FORWARD CHAINING")
    print("=" * 60)
    
    print("\n[1] SỰ KIỆN BAN ĐẦU (Facts):")
    for fact in sorted(kb.facts, key=lambda f: f.name):
        print(f"  • {fact}")
    
    print(f"\n[2] SỐ QUY TẮC: {len(kb.rules)}")
    for rule in sorted(kb.rules, key=lambda r: r.priority, reverse=True):
        print(f"  • {rule}")
    
    # Thực hiện suy luận
    engine = LogicInferenceEngine(kb)
    all_facts = engine.forward_chain()
    
    print(f"\n[3] KẾT QUẢ SAU SỰ LUẬN:")
    print(f"  • Tổng sự kiện: {len(all_facts)}")
    print(f"  • Quy tắc áp dụng: {len(engine.get_applied_rules())}")
    
    print(f"\n[4] DANH SÁCH TẤT CẢ SỰ KIỆN:")
    for fact in sorted(all_facts, key=lambda f: f.name):
        status = "🟢 Suy ra" if fact in engine.inferred_facts else "⚫ Gốc"
        print(f"  {status} | {fact}")
        explanation = engine.explain_conclusion(fact)
        if "Suy ra" in explanation:
            print(f"       {explanation}")
    
    print(f"\n[5] HÀNH ĐỘNG TỰ ĐỘNG HÓA:")
    # Tìm tất cả hành động (action predicates)
    actions = {fact for fact in all_facts if any(
        name in fact.name for name in ["light_on", "light_off", "ac_on", "door_locked", "energy_saving"]
    )}
    if actions:
        for action in sorted(actions, key=lambda a: a.name):
            print(f"  ⚡ {action}")
    else:
        print("  (Không có hành động tự động hóa)")
    
    print("\n" + "=" * 60)
