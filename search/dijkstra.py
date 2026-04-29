import heapq

def dijkstra(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    
    visited = set()
    parent = {}
    cost_so_far = {start: 0}
    
    nodes_expanded = 0
    
    while pq:
        cost, current = heapq.heappop(pq)
        
        if current == goal:
            break
        
        if current in visited:
            continue
        
        visited.add(current)
        nodes_expanded += 1
        
        for neighbor in grid.get_neighbors(current):  # FIX ở đây
            new_cost = cost + 1
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
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