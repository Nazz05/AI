# Cac ham ho tro cho thuat toan A*

def heuristic(a, b):
    """
    Tinh khoang cach Manhattan giua 2 diem
    
    Khoang cach Manhattan: |x1-x2| + |y1-y2|
    Day la do do "khoang cach theo huong" tu a den b
    Dung de ước tính chi phi con lai trong A*
    
    Tham so:
        a: Toa do diem hien tai, dang tuple (x1, y1)
        b: Toa do diem dich, dang tuple (x2, y2)
        
    Tra ve:
        Khoang cach Manhattan (int)
        
    Vi du:
        heuristic((0,0), (4,4)) = |0-4| + |0-4| = 8
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(came_from, current):
    """
    Tai tao duong di tu diem bat dau den diem dich
    
    Thuat toan:
        1. Bat dau tu diem dich (current)
        2. Tra lui theo ma tran "came_from" de tim diem truoc do
        3. Lap lai toi khi khong con diem truoc nua (la diem bat dau)
        4. Dao nguoc danh sach de co thu tu dung: tu dau den cuoi
    
    Tham so:
        came_from: Dict luu vi tri truoc do cua moi diem
                   Key: vi tri hien tai (x, y)
                   Value: vi tri truoc do
        current: Vi tri dich cuoi cung (x, y)
        
    Tra ve:
        Danh sach cac vi tri tao thanh duong di, tu START den GOAL
        
    Vi du:
        came_from = {(0,1): (0,0), (1,1): (0,1), ...}
        current = (4,4)
        => path = [(0,0), (0,1), (1,1), ..., (4,4)]
    """
    path = [current]  # Bat dau tu diem cuoi
    
    while current in came_from:  # Con co duong truoc
        current = came_from[current]  # Lui 1 buoc
        path.append(current)  # Them vao duong di
    
    return path[::-1]  # Dao nguoc de co thu tu dung