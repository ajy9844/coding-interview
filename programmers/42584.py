def solution(prices):
    answer = [0] * len(prices)
    stack = [[-1, 0]]
    
    for (i, p) in enumerate(prices):
        while True:
            ti, tp = stack[-1]
            if tp > p:
                stack.pop()
                answer[ti] = i - ti
            else:
                break
        stack.append([i, p])
    
    while stack:
        [i, p] = stack.pop()
        if i == -1: break
        answer[i] = (len(prices)-1) - i
    
    return answer
