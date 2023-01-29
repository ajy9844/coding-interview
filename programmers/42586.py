from collections import deque
import math

def solution(progresses, speeds):    
    answer = []
    queue = deque()
    
    for pair in zip(progresses, speeds):
        queue.append(math.ceil((100-pair[0])/pair[1]))
    
    max = queue[0]
    cnt = 0
    
    while queue:
        x = queue.popleft()
        if x <= max:
            cnt += 1
        else:
            answer.append(cnt)
            max = x
            cnt = 1
    answer.append(cnt)
    
    return answer
