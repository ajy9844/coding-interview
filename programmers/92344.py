def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    map = [[0 for _ in range(m)] for _ in range(n)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        map[r1][c1] += degree
        if r2+1 < n:
            map[r2+1][c1] += -degree
        if c2+1 < m:
            map[r1][c2+1] += -degree
        if r2+1 < n and c2+1 < m:
            map[r2+1][c2+1] += degree
    
    for r in range(n):
        for c in range(m-1):
            map[r][c+1] += map[r][c]
    
    for r in range(n-1):
        for c in range(m):
            map[r+1][c] += map[r][c]

    for r in range(n):
        for c in range(m):
            board[r][c] += map[r][c]
            if board[r][c] >= 1:
                answer += 1
    
    return answer
