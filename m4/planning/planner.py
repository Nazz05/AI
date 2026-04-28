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
    print("AI PLANNING - SMART HOME AUTOMATION (STRIPS/PDDL)")
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
    
    print("\n[1] TRẠNG THÁI BAN ĐẦU (Initial State):")
    for atom in sorted(initial_state, key=lambda a: a.name):
        print(f"  • {atom}")
    
    print(f"\n[2] TRẠNG THÁI MỤC TIÊU (Goal State):")
    for atom in sorted(goal_state, key=lambda a: a.name):
        print(f"  • {atom}")
    
    print(f"\n[3] DANH SÁCH CÁC HÀNH ĐỘNG KHẢ DỤNG: {len(actions)}")
    for i, action in enumerate(actions, 1):
        print(f"  {i}. {action}")
    
    # Tạo planner
    planner = STRIPSPlanner(initial_state, goal_state, actions)
    
    # Tìm kế hoạch
    print("\n[4] TÌM KIẾM KẾ HOẠCH (BFS)...")
    plan = planner.find_plan(method="bfs", max_depth=10)
    
    if plan:
        print(f"\n[5] KẾ HOẠCH TÌM ĐƯỢC: {len(plan)} bước")
        for step in planner.get_plan_steps():
            print(f"  {step}")
        
        # Thực thi kế hoạch
        print(f"\n[6] THỰC THI KẾ HOẠCH:")
        executor = PlanExecutor(plan)
        final_state = executor.execute_all(initial_state)
        
        if final_state:
            print(f"\n[7] TRẠNG THÁI CUỐI CÙNG: {len(final_state)} atoms")
            
            # Kiểm tra mục tiêu
            if goal_state.issubset(final_state):
                print("✓ ĐẠT MỤC TIÊU!")
            else:
                print("✗ CHƯA ĐẠT MỤC TIÊU")
                missing = goal_state - final_state
                print(f"  Còn thiếu: {missing}")
    else:
        print("✗ KHÔNG TÌM ĐƯỢC KẾ HOẠCH")
    
    print("\n" + "=" * 70)


def run_logistics_planning():
    """Chạy planner cho bài toán logistics"""
    
    print("=" * 70)
    print("AI PLANNING - LOGISTICS (STRIPS/PDDL)")
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
    
    print("\n[1] Trạng thái ban đầu:")
    for atom in initial_state:
        print(f"  • {atom}")
    
    print(f"\n[2] Trạng thái mục tiêu:")
    for atom in goal_state:
        print(f"  • {atom}")
    
    # Tạo planner
    planner = STRIPSPlanner(initial_state, goal_state, actions)
    
    # Tìm kế hoạch
    print("\n[3] Tìm kế hoạch...")
    plan = planner.find_plan(method="bfs", max_depth=10)
    
    if plan:
        print(f"\n[4] Kế hoạch: {len(plan)} bước")
        for step in planner.get_plan_steps():
            print(f"  {step}")
        
        # Thực thi
        print(f"\n[5] Thực thi kế hoạch:")
        executor = PlanExecutor(plan)
        final_state = executor.execute_all(initial_state)
        
        if final_state and goal_state.issubset(final_state):
            print("\n✓ ĐẠT MỤC TIÊU!")
    else:
        print("✗ KHÔNG TÌM ĐƯỢC KẾ HOẠCH")
    
    print("\n" + "=" * 70)
