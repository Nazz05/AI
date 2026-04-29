import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    
    visited = set()
    parent = {}
    
    nodes_expanded = 0
    
    while pq:
        _, current = heapq.heappop(pq)
        
        if current == goal:
            break
        
        if current in visited:
            continue
        
        visited.add(current)
        nodes_expanded += 1
        
        for neighbor in grid.get_neighbors(current):  # FIX ở đây
            if neighbor not in visited:
                h = heuristic(neighbor, goal)
                heapq.heappush(pq, (h, neighbor))
                parent[neighbor] = current
    
    path = []
    cur = goal
    
    while cur != start:
        if cur not in parent:
            return [], nodes_expanded
        path.append(cur)
        cur = parent[cur]
    
    path.append(start)
    path.reverse()
    
    return path, nodes_expanded