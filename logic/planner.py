# ===================================
# PLANNER - LẬP KẾ HOẠCH
# ===================================
# Tích hợp STRIPS để lập kế hoạch cho bài toán nhà thông minh

from typing import Set, List
from .strips import Atom, STRIPSPlanner, PlanExecutor
from .domain import create_smart_home_domain, create_logistics_domain


def run_smart_home_planning():
    """Chạy planner cho bài toán nhà thông minh"""
    
    print("=" * 70)
    print("LAP KE HOACH AI - TU DONG HOA NHA THONG MINH (STRIPS/PDDL)")
    print("=" * 70)
    
    # Lấy domain
    domain = create_smart_home_domain()
    atoms = domain["atoms"]
    actions = domain["actions"]
    
    # Định nghĩa trạng thái ban đầu
    initial_state = {
        atoms["person_home"],
        atoms["dark"],
        atoms["light_off"],
        atoms["ac_off"],
        atoms["door_unlocked"],
        atoms["security_disarmed"],
        atoms["low_temperature"]
    }
    
    # Định nghĩa mục tiêu (goal)
    goal_state = {
        atoms["person_home"],
        atoms["light_on"],      # Cần bật đèn
        atoms["ac_off"],        # AC tắt
        atoms["door_locked"],   # Cửa khóa
        atoms["security_disarmed"]  # Bảo mật vô hiệu
    }
    
    print("\n[1] TRANG THAI BAN DAU:")
    for atom in sorted(initial_state, key=lambda a: a.name):
        print(f"  - {atom}")
    
    print(f"\n[2] TRANG THAI MUC TIEU:")
    for atom in sorted(goal_state, key=lambda a: a.name):
        print(f"  - {atom}")
    
    print(f"\n[3] HANH DONG CO SAN: {len(actions)}")
    for i, action in enumerate(actions, 1):
        print(f"  {i}. {action}")
    
    # Tạo planner
    planner = STRIPSPlanner(initial_state, goal_state, actions)
    
    # Find plan
    print("\n[4] DANG TIM KE HOACH (BFS)...")
    plan = planner.find_plan(method="bfs", max_depth=10)
    
    if plan:
        print(f"\n[5] KE HOACH TIM THAY: {len(plan)} buoc")
        for step in planner.get_plan_steps():
            print(f"  {step}")
        
        # Execute plan
        print(f"\n[6] THUC THI KE HOACH:")
        executor = PlanExecutor(plan)
        final_state = executor.execute_all(initial_state)
        
        if final_state:
            print(f"\n[7] TRANG THAI CUOI CUNG: {len(final_state)} atoms")
            
            # Check goal
            if goal_state.issubset(final_state):
                print("DAT DUOC MUC TIEU!")
            else:
                print("KHONG DAT DUOC MUC TIEU")
                missing = goal_state - final_state
                print(f"  Thieu: {missing}")
    else:
        print("KHONG TIM THAY KE HOACH")
    
    print("\n" + "=" * 70)


def run_logistics_planning():
    """Chạy planner cho bài toán logistics"""
    
    print("=" * 70)
    print("LAP KE HOACH AI - VAN TAI (STRIPS/PDDL)")
    print("=" * 70)
    
    # Lấy domain
    domain = create_logistics_domain()
    atoms = domain["atoms"]
    actions = domain["actions"]
    
    # Trạng thái ban đầu: hàng ở A, xe ở A
    initial_state = {
        atoms["at_A"],
        atoms["at_truck_A"],
        atoms["unloaded"]
    }
    
    # Mục tiêu: hàng ở B, xe ở B
    goal_state = {
        atoms["at_B"],
        atoms["at_truck_B"],
        atoms["unloaded"]
    }
    
    print("\n[1] Trang thai ban dau:")
    for atom in initial_state:
        print(f"  - {atom}")
    
    print(f"\n[2] Trang thai muc tieu:")
    for atom in goal_state:
        print(f"  - {atom}")
    
    # Tạo planner
    planner = STRIPSPlanner(initial_state, goal_state, actions)
    
    # Find plan
    print("\n[3] Dang tim ke hoach...")
    plan = planner.find_plan(method="bfs", max_depth=10)
    
    if plan:
        print(f"\n[4] Ke hoach tim thay: {len(plan)} buoc")
        for step in planner.get_plan_steps():
            print(f"  {step}")
        
        # Execute plan
        print(f"\n[5] Thuc thi ke hoach:")
        executor = PlanExecutor(plan)
        final_state = executor.execute_all(initial_state)
        
        if final_state and goal_state.issubset(final_state):
            print("Dat duoc muc tieu!")
    else:
        print("Khong tim thay ke hoach")
    
    print("\n" + "=" * 70)
