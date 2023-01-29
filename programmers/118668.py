from queue import PriorityQueue

def dijkstra(src, dst, item):
    sy, sx = src[0], src[1]
    dy, dx = dst[0], dst[1]
    
    queue = PriorityQueue()
    dist = [[1000 for col in range(dx+1)] for row in range(dy+1)]
    visited = [[0 for col in range(dx+1)] for row in range(dy+1)]
    
    dist[sy][sx] = 0
    queue.put((0, src))
    
    while not queue.empty():
        cost, [vy, vx] = queue.get()
        visited[vy][vx] = 1
        
        if vy == dy and vx == dx:
            break
        
        #1. y축으로 +1 이동
        cy, cx = vy+1, vx
        if (cy >= 0 and cy <= dy) and (cx >= 0 and cx <= dx):
            if (not visited[cy][cx]) and (cost+1 < dist[cy][cx]):
                dist[cy][cx] = cost+1
                queue.put((cost+1, [cy,cx]))
        
        #2. x축으로 +1 이동
        cy, cx = vy, vx+1
        if (cy >= 0 and cy <= dy) and (cx >= 0 and cx <= dx):
            if (not visited[cy][cx]) and (cost+1 < dist[cy][cx]):
                dist[cy][cx] = cost+1
                queue.put((cost+1, [cy,cx]))
        
        #3. y축으로 +a 만큼, x축으로 +b 만큼 이동
        for y_req, x_req, y_rwd, x_rwd, w in item:
            if vy >= y_req and vx >= x_req:
                cy = dy if vy+y_rwd >= dy else vy+y_rwd
                cx = dx if vx+x_rwd >= dx else vx+x_rwd
                
                if (cy >= 0 and cy <= dy) and (cx >= 0 and cx <= dx):
                    if (not visited[cy][cx]) and (cost+w < dist[cy][cx]):
                        dist[cy][cx] = cost+w
                        queue.put((cost+w, [cy,cx]))
    
    return dist[dy][dx]

def solution(alp, cop, problems):
    alp_max = max([x[0] for x in problems])
    cop_max = max([x[1] for x in problems])
    
    src = [alp_max if alp >= alp_max else alp, cop_max if cop >= cop_max else cop]
    dst = [alp_max, cop_max]
    
    answer = dijkstra(src, dst, problems)
    
    return answer
