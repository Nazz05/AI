# ===================================
# ĐỊNH NGHĨA DOMAIN STRIPS/PDDL
# ===================================
# Biểu diễn domain bằng STRIPS (Stanford Research Institute Problem Solver)
# Domain định nghĩa: Predicates, Actions, Preconditions, Effects

from typing import Set, List, Callable
from dataclasses import dataclass
from .strips import Atom, Action


# ===================================
# ATOMS (Vị từ cơ bản)
# ===================================

def create_smart_home_domain():
    """Tạo domain cho bài toán nhà thông minh"""
    
    # Định nghĩa các atoms (facts)
    atoms = {
        # Vị trí & sự kiện quan sát
        "person_home": Atom("person_home", []),
        "person_away": Atom("person_away", []),
        "dark": Atom("dark", []),
        "bright": Atom("bright", []),
        "motion_detected": Atom("motion_detected", []),
        "high_temperature": Atom("high_temperature", []),
        "low_temperature": Atom("low_temperature", []),
        
        # Trạng thái thiết bị
        "light_on": Atom("light_on", []),
        "light_off": Atom("light_off", []),
        "ac_on": Atom("ac_on", []),
        "ac_off": Atom("ac_off", []),
        "door_locked": Atom("door_locked", []),
        "door_unlocked": Atom("door_unlocked", []),
        "security_armed": Atom("security_armed", []),
        "security_disarmed": Atom("security_disarmed", []),
    }
    
    # Định nghĩa các actions (hành động)
    actions = []
    
    # ACTION 1: Bật đèn
    action_turn_on_light = Action(
        name="turn_on_light",
        preconditions=[atoms["dark"], atoms["person_home"]],
        effects=[
            (atoms["light_on"], True),
            (atoms["light_off"], False)
        ]
    )
    actions.append(action_turn_on_light)
    
    # ACTION 2: Tắt đèn
    action_turn_off_light = Action(
        name="turn_off_light",
        preconditions=[atoms["light_on"]],
        effects=[
            (atoms["light_off"], True),
            (atoms["light_on"], False)
        ]
    )
    actions.append(action_turn_off_light)
    
    # ACTION 3: Bật điều hòa
    action_turn_on_ac = Action(
        name="turn_on_ac",
        preconditions=[atoms["high_temperature"]],
        effects=[
            (atoms["ac_on"], True),
            (atoms["ac_off"], False)
        ]
    )
    actions.append(action_turn_on_ac)
    
    # ACTION 4: Tắt điều hòa
    action_turn_off_ac = Action(
        name="turn_off_ac",
        preconditions=[atoms["ac_on"], atoms["low_temperature"]],
        effects=[
            (atoms["ac_off"], True),
            (atoms["ac_on"], False)
        ]
    )
    actions.append(action_turn_off_ac)
    
    # ACTION 5: Khóa cửa
    action_lock_door = Action(
        name="lock_door",
        preconditions=[atoms["door_unlocked"]],
        effects=[
            (atoms["door_locked"], True),
            (atoms["door_unlocked"], False)
        ]
    )
    actions.append(action_lock_door)
    
    # ACTION 6: Mở khóa cửa
    action_unlock_door = Action(
        name="unlock_door",
        preconditions=[atoms["person_home"]],
        effects=[
            (atoms["door_unlocked"], True),
            (atoms["door_locked"], False)
        ]
    )
    actions.append(action_unlock_door)
    
    # ACTION 7: Kích hoạt chế độ bảo mật
    action_arm_security = Action(
        name="arm_security",
        preconditions=[atoms["person_away"], atoms["door_locked"]],
        effects=[
            (atoms["security_armed"], True),
            (atoms["security_disarmed"], False)
        ]
    )
    actions.append(action_arm_security)
    
    # ACTION 8: Vô hiệu hóa chế độ bảo mật
    action_disarm_security = Action(
        name="disarm_security",
        preconditions=[atoms["person_home"]],
        effects=[
            (atoms["security_disarmed"], True),
            (atoms["security_armed"], False)
        ]
    )
    actions.append(action_disarm_security)
    
    return {
        "atoms": atoms,
        "actions": actions
    }


def create_logistics_domain():
    """Tạo domain cho bài toán logistics (ví dụ khác)
    Bài toán: Vận chuyển hàng hóa giữa các địa điểm
    """
    
    # Atoms
    atoms = {
        "at_A": Atom("at_A", []),
        "at_B": Atom("at_B", []),
        "at_C": Atom("at_C", []),
        "at_truck_A": Atom("at_truck_A", []),
        "at_truck_B": Atom("at_truck_B", []),
        "in_truck": Atom("in_truck", []),
        "unloaded": Atom("unloaded", []),
    }
    
    # Actions
    actions = []
    
    # Chất hàng lên xe tải
    action_load_truck = Action(
        name="load_truck",
        preconditions=[atoms["at_A"], atoms["at_truck_A"], atoms["unloaded"]],
        effects=[
            (atoms["in_truck"], True),
            (atoms["unloaded"], False)
        ]
    )
    actions.append(action_load_truck)
    
    # Vận chuyển tới B
    action_transport_to_B = Action(
        name="transport_to_B",
        preconditions=[atoms["at_truck_A"], atoms["in_truck"]],
        effects=[
            (atoms["at_truck_B"], True),
            (atoms["at_truck_A"], False),
            (atoms["at_B"], True),
            (atoms["at_A"], False)
        ]
    )
    actions.append(action_transport_to_B)
    
    # Bỏ hàng xuống
    action_unload = Action(
        name="unload",
        preconditions=[atoms["in_truck"]],
        effects=[
            (atoms["unloaded"], True),
            (atoms["in_truck"], False)
        ]
    )
    actions.append(action_unload)
    
    return {
        "atoms": atoms,
        "actions": actions
    }
