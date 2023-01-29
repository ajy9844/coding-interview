from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0
    
    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break
    
    return answer
