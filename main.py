# ===================================
# CHUONG TRINH CHINH
# ===================================
# Day la diem vao cua ung dung
# Toi day se: Khoi tao the gioi, chay A*, va hien thi ket qua

from core.grid import GridWorld
from config import GRID, START, GOAL
from search.astar import astar
from visualization.plot import draw

def main():
    """
    Chuong trinh chinh: Chay thuat toan A* de tim duong di
    """
    
    # BUOC 1: Khoi tao the gioi
    # Tao doi tuong GridWorld tu ma tran GRID trong config
    grid = GridWorld(GRID)

    # BUOC 2: Chay thuat toan A*
    # Tim duong di ngan nhat tu START den GOAL
    path = astar(grid, START, GOAL)

    # BUOC 3: Xu ly ket qua
    if path:
        # Neu tim duoc duong
        print("Path found!")
        print("Path:", path)
        print("Length:", len(path))
        
        # BUOC 4: Hien thi duong di bang do thi
        try:
            draw(grid, path)
        except Exception as e:
            # Neu matplotlib co loi, chi bao loi nhung khong dung chuong trinh
            print(f"Visualization error: {e}")
    else:
        # Neu khong tim duoc duong
        print("No path found!")

if __name__ == "__main__":
    # Chay chuong trinh khi file nay duoc thuc thi truc tiep
    main()