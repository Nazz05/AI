# ===================================
# CHUONG TRINH CHINH
# ===================================
# Day la diem vao cua ung dung
# Toi day se:
# - M1: Chay A* de tim duong di
# - M3: Chay Random Search + Q-learning
# - M4: Chay Logic + STRIPS

from core.grid import GridWorld
from config import GRID, START, GOAL
from search.astar import astar
from visualization.plot import draw
from m3.q_learning import run_q_learning
from m3.random_search import run_random_search
from m3.visualize import plot_training_results, print_q_table
from logic.rules import create_smart_home_kb
from logic.inference import run_inference
from logic.planner import run_smart_home_planning


def run_m1_astar():
    """
    M1: Thuat toan A* de tim duong di ngan nhat
    """
    print("\n" + "=" * 70)
    print("MEMBER M1: A* PATHFINDING ALGORITHM")
    print("=" * 70)

    grid = GridWorld(GRID)
    print("\n[1] Khoi tao luoi 5x5")

    print("[2] Chay thuat toan A*...")
    path = astar(grid, START, GOAL)

    if path:
        print("\n[3] Ket qua:")
        print("  - Path found!")
        print(f"  - Path: {path}")
        print(f"  - Length: {len(path)} steps")

        print("\n[4] Hien thi bieu do...")
        try:
            draw(grid, path)
        except Exception as e:
            print(f"Visualization error: {e}")
    else:
        print("  - No path found!")

    print("\n" + "=" * 70)


def run_m3_random_q_learning():
    """
    M3: Random Search + Q-learning tren GridWorld.
    """
    print("\n" + "=" * 70)
    print("MEMBER M3: RANDOM SEARCH + Q-LEARNING")
    print("=" * 70)

    print("\n[1] RANDOM SEARCH - TIM DUONG NGAU NHIEN")
    print("  - Quy uoc reward: den dich = +100, di hop le moi buoc = -1, dam tuong/di sai = -5.")
    print("  - Vi vay reward cang cao thi duong di cang tot; reward am lon cho thay robot di long vong hoac va vao tuong nhieu.")
    random_result = run_random_search()
    success_rate = (random_result["successful_episodes"] / random_result["episodes"]) * 100
    print(f"  - So lan chay: {random_result['episodes']}")
    print(f"  - So lan thanh cong: {random_result['successful_episodes']}")
    print(f"  - Ty le thanh cong: {success_rate:.1f}%")
    print("  - Mot vai lan chay mau:")
    for log in random_result["logs"][:10]:
        status = "Thanh cong" if log["success"] else "That bai"
        print(
            f"    Lan {log['episode']}: {status} | So buoc = {log['steps']} | Tong reward = {log['reward']}"
        )
    if random_result["best_path"]:
        print(f"  - Duong di tot nhat tim duoc: {random_result['best_path']}")
        print(f"  - Do dai duong di tot nhat: {len(random_result['best_path'])} nut")
        print(f"  - So buoc de den dich: {random_result['best_steps']}")
        print("  - Nhan xet: Random Search co the tim thay duong di, nhung ket qua khong on dinh va thuong di vong.")
    else:
        print("  - Khong tim thay duong di trong cac episode da chay.")

    print("\n[2] Q-LEARNING - HOC DUONG DI")
    print("  - Q-learning hoc bang cach cap nhat gia tri Q cho tung trang thai va hanh dong.")
    print("  - Muc tieu la toi uu tong reward trong tuong lai, tu do tim ra duong di tot den dich.")
    q_result = run_q_learning()
    q_success_rate = (q_result["successful_episodes"] / len(q_result["success_history"])) * 100
    print(f"  - So episode huan luyen: {len(q_result['success_history'])}")
    print(f"  - So episode thanh cong: {q_result['successful_episodes']}")
    print(f"  - Ty le thanh cong sau huan luyen: {q_success_rate:.1f}%")
    print(f"  - Agent co tim duoc chinh sach tot khong: {'Co' if q_result['solved'] else 'Khong'}")
    if q_result["learned_path"]:
        print(f"  - Duong di sau khi hoc: {q_result['learned_path']}")
        print(f"  - Do dai duong di sau khi hoc: {len(q_result['learned_path'])} nut")
        print("  - Nhan xet: Q-learning da hoc duoc cach di den dich mot cach on dinh.")
    else:
        print("  - Chua trich xuat duoc duong di tu Q-table.")

    print("\n[3] SO SANH A* VA Q-LEARNING")
    grid = GridWorld(GRID)
    astar_path = astar(grid, START, GOAL)
    if astar_path:
        print(f"  - Duong di A*: {astar_path}")
        print(f"  - Do dai duong di A*: {len(astar_path)} nut")
    else:
        print("  - A* khong tim thay duong di.")

    if q_result["learned_path"]:
        print(f"  - Do dai duong di Q-learning: {len(q_result['learned_path'])} nut")
        if astar_path and len(astar_path) == len(q_result["learned_path"]):
            print("  - Nhan xet: Q-learning hoc duoc duong di toi uu tuong duong A* tren grid nay.")
        else:
            print("  - Nhan xet: Q-learning tim duoc duong di hop le nhung chua bang A*.")
    else:
        print("  - Q-learning chua tim duoc path hop le.")

    print("\n[4] GIAI THICH BANG Q-LEARNING")
    print("  - Moi dong co dang: (x, y) -> 0, 1, 2, 3")
    print("  - Trong do: 0 = UP, 1 = DOWN, 2 = LEFT, 3 = RIGHT")
    print("  - Gia tri Q cang lon thi hanh dong do cang nen duoc chon tai vi tri tuong ung.")
    print("  - Vi du neu o (0, 0) action 3 co gia tri lon nhat, agent se uu tien di sang phai.")
    print_q_table(q_result["q_table"])

    print("\n[5] BIEU DO Q-LEARNING")
    print("  - Reward tang dan cho thay agent hoc tot hon qua tung episode.")
    print("  - So buoc giam dan cho thay agent tim duoc duong di hieu qua hon.")
    print("  - Success rate tang dan cho thay kha nang den dich ngay cang on dinh.")
    try:
        plot_training_results(
            q_result["reward_history"],
            q_result["step_history"],
            q_result["success_history"],
        )
    except Exception as e:
        print(f"Visualization error: {e}")

    if q_result["learned_path"]:
        print("\n[6] MINH HOA DUONG DI Q-LEARNING")
        print("  - Cua so do thi se hien thi duong di ma agent hoc duoc tren GridWorld.")
        try:
            draw(GridWorld(GRID), q_result["learned_path"])
        except Exception as e:
            print(f"Visualization error: {e}")

    print("\n" + "=" * 70)


def run_m4_logic_planning():
    """
    M4: He thong Logic + Lap ke hoach AI (STRIPS/PDDL)
    """
    print("\n" + "=" * 70)
    print("MEMBER M4: LOGIC + STRIPS")
    print("=" * 70)

    print("\n" + "=" * 70)
    print("PART 1: LOGIC INFERENCE ENGINE - SMART HOME AUTOMATION")
    print("=" * 70)

    kb = create_smart_home_kb()
    run_inference(kb)

    print("\n" + "=" * 70)
    print("PART 2: STRIPS PLANNING - GOAL-BASED ACTION PLANNING")
    print("=" * 70)

    run_smart_home_planning()


def display_menu():
    """Hien thi menu chon chuong trinh"""
    print("\n" + "=" * 70)
    print("AI PROJECT - MENU CHINH")
    print("=" * 70)
    print("\nChon chuong trinh can chay:")
    print("  1. M1: A* Pathfinding Algorithm")
    print("  2. M3: Random Search + Q-learning")
    print("  3. M4: Logic + STRIPS")
    print("  4. Chay tat ca")
    print("  0. Thoat")
    print("\n" + "=" * 70)


def main():
    """Ham main"""
    while True:
        display_menu()
        choice = input("\nNhap lua chon (0-4): ").strip()

        if choice == "1":
            run_m1_astar()
        elif choice == "2":
            run_m3_random_q_learning()
        elif choice == "3":
            run_m4_logic_planning()
        elif choice == "4":
            run_m1_astar()
            run_m3_random_q_learning()
            run_m4_logic_planning()
        elif choice == "0":
            print("\nTam biet!")
            break
        else:
            print("Lua chon khong hop le. Vui long chon lai.")


if __name__ == "__main__":
    main()
