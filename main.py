# ===================================
# CHUONG TRINH CHINH
# ===================================
# Day la diem vao cua ung dung
# Toi day se: 
# - M1: Chay A* de tim duong di
# - M4: Chay Logic + Planning (STRIPS/PDDL)

from core.grid import GridWorld
from config import GRID, START, GOAL
from search.astar import astar
from visualization.plot import draw
from m4.logic.rules import create_smart_home_kb
from m4.logic.inference import run_inference
from m4.planning.planner import run_smart_home_planning, run_logistics_planning


def run_m1_astar():
    """
    M1: Thuat toan A* de tim duong di ngan nhat
    """
    print("\n" + "=" * 70)
    print("MEMBER M1: A* PATHFINDING ALGORITHM")
    print("=" * 70)
    
    # BUOC 1: Khoi tao the gioi
    grid = GridWorld(GRID)
    print("\n[1] Khởi tạo lưới 5x5")

    # BUOC 2: Chay thuat toan A*
    print("[2] Chạy thuật toán A*...")
    path = astar(grid, START, GOAL)

    # BUOC 3: Xu ly ket qua
    if path:
        print("\n[3] Kết quả:")
        print(f"  ✓ Path found!")
        print(f"  • Path: {path}")
        print(f"  • Length: {len(path)} steps")
        
        # BUOC 4: Hien thi duong di bang do thi
        print("\n[4] Hiển thị biểu đồ...")
        try:
            draw(grid, path)
        except Exception as e:
            print(f"Visualization error: {e}")
    else:
        print("✗ No path found!")
    
    print("\n" + "=" * 70)


def run_m4_logic_planning():
    """
    M4: Hệ thống Logic + Lập kế hoạch AI (STRIPS/PDDL)
    Gồm 2 phần chuẩn:
    - Phần 1: Forward Chaining Logic Inference (tự động hóa nhà thông minh)
    - Phần 2: STRIPS Planning (lập kế hoạch hành động cho nhà thông minh)
    """
    print("\n" + "=" * 70)
    print("MEMBER M4: LOGIC + AI PLANNING (STRIPS/PDDL)")
    print("=" * 70)
    
    # PHẦN 1: LOGIC INFERENCE
    print("\n" + "=" * 70)
    print("PART 1: LOGIC INFERENCE ENGINE - SMART HOME AUTOMATION")
    print("=" * 70)
    
    # Tạo cơ sở kiến thức cho nhà thông minh
    kb = create_smart_home_kb()
    
    # Chạy inference engine
    run_inference(kb)
    
    # PHẦN 2: STRIPS PLANNING
    print("\n" + "=" * 70)
    print("PART 2: STRIPS PLANNING - GOAL-BASED ACTION PLANNING")
    print("=" * 70)
    
    # Bài toán chuẩn: Nhà thông minh
    run_smart_home_planning()


def display_menu():
    """Hiển thị menu chọn chương trình"""
    print("\n" + "=" * 70)
    print("AI PROJECT - MENU CHÍNH")
    print("=" * 70)
    print("\nChọn chương trình cần chạy:")
    print("  1. M1: A* Pathfinding Algorithm")
    print("  2. M4: Logic + AI Planning (STRIPS/PDDL)")
    print("  3. Chạy tất cả")
    print("  0. Thoát")
    print("\n" + "=" * 70)


def main():
    """Hàm main"""
    while True:
        display_menu()
        choice = input("\nNhập lựa chọn (0-3): ").strip()
        
        if choice == "1":
            run_m1_astar()
        elif choice == "2":
            run_m4_logic_planning()
        elif choice == "3":
            run_m1_astar()
            run_m4_logic_planning()
        elif choice == "0":
            print("\nTạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    # Chay chuong trinh khi file nay duoc thuc thi truc tiep
    main()