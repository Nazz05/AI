import heapq
from core.utils import heuristic, reconstruct_path

# Thuat toan A* - Tim duong di ngan nhat trong luoi

def astar(grid, start, goal):
    """
    Thuat toan A*: Tim duong di ngan nhat tu start den goal
    
    Thuat toan hoat dong:
        1. Khoi tao tap open_set chua cac diem can kiem tra
        2. Lap cho den khi open_set rong:
           a. Lay diem co F-score nho nhat (ưu tien)
           b. Neu la diem dich, tra ve duong di
           c. Kiem tra cac hang xom va cap nhat chi phi
        3. Neu khong tim duoc, tra ve None
    
    Cac thong so:
        g_score: Chi phi tu START den diem hien tai
        f_score: g_score + heuristic(hien tai, GOAL)
                 (chi phi thuc te + ước tính con lai)
    
    Tham so:
        grid: Doi tuong GridWorld
        start: Vi tri bat dau (x, y)
        goal: Vi tri dich (x, y)
        
    Tra ve:
        - Danh sach cac vi tri tao thanh duong di ngan nhat
        - None neu khong tim duoc duong di
    """
    
    # Tap hop cac diem can kiem tra
    # Luu dung: (f_score, vi_tri)
    # heapq giup ta lay diem co f_score nho nhat
    open_set = []
    heapq.heappush(open_set, (0, start))

    # Luu tru: vi tri dung truoc -> diem hien tai
    # Dung de tai tao duong di
    came_from = {}
    
    # g_score: Chi phi tu START den diem
    # Key: vi tri (x, y)
    # Value: chi phi (so buoc)
    g_score = {start: 0}
    
    # Track visited nodes
    visited = set()
    
    # Count expanded nodes
    nodes_expanded = 0

    # Lap chinh: A* search
    while open_set:
        # Lay diem co f_score nho nhat
        _, current = heapq.heappop(open_set)

        # Skip if already visited
        if current in visited:
            continue
        
        visited.add(current)
        nodes_expanded += 1

        # Neu da toi diem dich: tra ve duong di
        if current == goal:
            return reconstruct_path(came_from, current), nodes_expanded

        # Kiem tra cac diem hang xom
        for neighbor in grid.get_neighbors(current):
            # g_score moi neu di qua diem hien tai
            # Chi phi = chi phi den hien tai + 1 (1 buoc)
            temp_g = g_score[current] + 1

            # Neu chua co duong toi neighbor, hoac duong moi ngan hon
            if neighbor not in g_score or temp_g < g_score[neighbor]:
                # Cap nhat chi phi
                g_score[neighbor] = temp_g
                
                # Tinh f_score = g + h
                # g: chi phi thuc te
                # h: ước tính khoang cach con lai
                f = temp_g + heuristic(neighbor, goal)
                
                # Them vao hang doi
                heapq.heappush(open_set, (f, neighbor))
                
                # Luu duong truoc
                came_from[neighbor] = current

    # Neu thoat vong lap ma open_set rong: khong co duong
    return None, nodes_expanded