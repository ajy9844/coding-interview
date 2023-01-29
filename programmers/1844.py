from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    dir = [[+1,0], [-1,0], [0,-1], [0,+1]]
    
    queue = deque([[0,0,1]])
    maps[0][0] = 0
    
    while queue:
        vy, vx, cnt = queue.popleft()
        for dy, dx in dir:
            cy, cx = vy + dy, vx + dx
            
            if (cy >= 0 and cy < n) and (cx >= 0 and cx < m):
                if cy == n-1 and cx == m-1:
                    maps[cy][cx] = 0
                    answer = cnt+1
                    break
                    
                if maps[cy][cx] == 1:
                    maps[cy][cx] = 0    
                    queue.append([cy, cx, cnt+1])
    
    return answer if maps[n-1][m-1] == 0 else -1
