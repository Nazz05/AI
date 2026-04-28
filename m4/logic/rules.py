# ===================================
# HỆ THỐNG LUẬT LOGIC - SMART HOME AUTOMATION
# ===================================
# Mô phỏng tự động hóa nhà thông minh
# Biểu diễn các quy tắc dưới dạng logic FOL (First Order Logic)
# Ví dụ: Nếu trời tối (dark) và có người (person_home), thì bật đèn (turn_light_on)

from typing import Dict, Set, List, Tuple
from dataclasses import dataclass, field

@dataclass
class Predicate:
    """Biểu diễn một vị từ trong logic (Fact)
    Ví dụ: dark(living_room), temperature(23), person_at(alice, kitchen)
    """
    name: str  # Tên vị từ
    args: Tuple[str, ...] = field(default_factory=tuple)  # Đối số
    
    def __hash__(self):
        return hash((self.name, self.args))
    
    def __eq__(self, other):
        if not isinstance(other, Predicate):
            return False
        return self.name == other.name and self.args == other.args
    
    def __repr__(self):
        if self.args:
            return f"{self.name}({', '.join(self.args)})"
        return self.name


@dataclass
class Rule:
    """Biểu diễn một quy tắc logic
    Dạng: Nếu {conditions} thì {conclusions}
    Ví dụ: Nếu dark(X) ∧ person_at(alice, X) → turn_light_on(X)
    """
    name: str
    conditions: List[Predicate]  # Điều kiện (premises)
    conclusions: List[Predicate]  # Kết luận (consequences)
    priority: int = 1  # Độ ưu tiên (cao hơn = thực thi trước)
    
    def __repr__(self):
        cond_str = " ∧ ".join(str(c) for c in self.conditions)
        conc_str = " ∧ ".join(str(c) for c in self.conclusions)
        return f"{self.name}: [{cond_str}] → [{conc_str}]"


class KnowledgeBase:
    """Cơ sở kiến thức chứa tất cả các sự kiện và quy tắc"""
    
    def __init__(self):
        self.facts: Set[Predicate] = set()  # Tập hợp các sự kiện (facts)
        self.rules: List[Rule] = []  # Danh sách các quy tắc
    
    def add_fact(self, predicate: Predicate):
        """Thêm một sự kiện vào cơ sở kiến thức"""
        self.facts.add(predicate)
    
    def add_rule(self, rule: Rule):
        """Thêm một quy tắc vào cơ sở kiến thức"""
        self.rules.append(rule)
    
    def remove_fact(self, predicate: Predicate):
        """Xóa một sự kiện khỏi cơ sở kiến thức"""
        self.facts.discard(predicate)
    
    def has_fact(self, predicate: Predicate) -> bool:
        """Kiểm tra sự kiện có tồn tại không"""
        return predicate in self.facts
    
    def get_facts_by_name(self, name: str) -> Set[Predicate]:
        """Lấy tất cả các sự kiện có tên nhất định"""
        return {fact for fact in self.facts if fact.name == name}
    
    def __repr__(self):
        return f"KnowledgeBase(facts={len(self.facts)}, rules={len(self.rules)})"


# ===================================
# VÍ DỤ: CẤU HÌNH SMART HOME
# ===================================

def create_smart_home_kb() -> KnowledgeBase:
    """Tạo cơ sở kiến thức cho hệ thống nhà thông minh"""
    kb = KnowledgeBase()
    
    # ============= FACTS (Sự kiện ban đầu) =============
    # Trạng thái các phòng
    kb.add_fact(Predicate("room", ("living_room",)))
    kb.add_fact(Predicate("room", ("bedroom",)))
    kb.add_fact(Predicate("room", ("kitchen",)))
    
    # Trạng thái ban đầu
    kb.add_fact(Predicate("person_home", ()))  # Có người ở nhà
    kb.add_fact(Predicate("dark", ("living_room",)))  # Phòng khách tối
    kb.add_fact(Predicate("temperature", ("20",)))  # Nhiệt độ 20°C
    kb.add_fact(Predicate("motion_detected", ("living_room",)))  # Phát hiện chuyển động
    
    # ============= RULES (Quy tắc logic) =============
    
    # RULE 1: Nếu phòng tối + có người ở nhà → bật đèn
    rule1 = Rule(
        name="Auto_Light_On",
        conditions=[
            Predicate("dark", ("living_room",)),
            Predicate("person_home", ())
        ],
        conclusions=[
            Predicate("light_on", ("living_room",))
        ],
        priority=2
    )
    kb.add_rule(rule1)
    
    # RULE 2: Nếu không phát hiện chuyển động + vắng nhà → tắt đèn
    rule2 = Rule(
        name="Auto_Light_Off",
        conditions=[
            Predicate("light_on", ("living_room",)),
            Predicate("no_motion", ("living_room",))
        ],
        conclusions=[
            Predicate("light_off", ("living_room",))
        ],
        priority=1
    )
    kb.add_rule(rule2)
    
    # RULE 3: Nếu nhiệt độ > 25 → bật điều hòa
    rule3 = Rule(
        name="Auto_AC_On",
        conditions=[
            Predicate("high_temperature", ())
        ],
        conclusions=[
            Predicate("ac_on", ())
        ],
        priority=2
    )
    kb.add_rule(rule3)
    
    # RULE 4: Nếu phát hiện chuyển động → bật đèn
    rule4 = Rule(
        name="Motion_Activated_Light",
        conditions=[
            Predicate("motion_detected", ("living_room",))
        ],
        conclusions=[
            Predicate("light_on", ("living_room",))
        ],
        priority=3
    )
    kb.add_rule(rule4)
    
    # RULE 5: Nếu vắng nhà → khóa cửa + bật chế độ tiết kiệm
    rule5 = Rule(
        name="Away_Mode_Activated",
        conditions=[
            Predicate("no_person_home", ())
        ],
        conclusions=[
            Predicate("door_locked", ()),
            Predicate("energy_saving_mode", ())
        ],
        priority=2
    )
    kb.add_rule(rule5)
    
    return kb
