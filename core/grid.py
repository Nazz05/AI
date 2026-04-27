# Lop dai dien the gioi - grid dang ma tran

class GridWorld:
    """
    Lop GridWorld: Dai dien the gioi duoi dang luoi (grid)
    - Chua grid nhan vao tu config
    - Cung cap cac phuong thuc kiem tra vi tri va tim hang xom
    """
    
    def __init__(self, grid):
        """
        Khoi tao GridWorld
        
        Tham so:
            grid: Ma tran 2D (list cua list)
                  0 = o trong (di duoc)
                  1 = tuong (di khong duoc)
        """
        self.grid = grid
        self.rows = len(grid)      # So hang trong grid
        self.cols = len(grid[0])   # So cot trong grid

    def is_valid(self, x, y):
        """
        Kiem tra xem vi tri (x, y) co hop le khong
        
        Tham so:
            x: Chi so hang
            y: Chi so cot
            
        Tra ve:
            True: Vi tri hop le va la o trong (= 0)
            False: Vi tri ngoai ranh gioi hoac la tuong (= 1)
        """
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0

    def get_neighbors(self, node):
        """
        Lay toan bo cac vi tri hang xom co the di chuyen toi
        
        Tham so:
            node: Vi tri hien tai dang co dang tuple (x, y)
            
        Tra ve:
            Danh sach cac vi tri hang xom hop le co the di toi
            
        Ghi chu:
            - Chi di tren duoi trai phai (4 huong)
            - Khong di cheo (8 huong)
        """
        x, y = node
        
        # 4 huong co the di: phai, duoi, trai, tren
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        result = []

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):  # Chi them vao neu hop le
                result.append((nx, ny))

        return result