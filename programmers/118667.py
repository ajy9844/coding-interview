from collections import deque

def solution(queue1, queue2):
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    
    sum1 = sum(dq1)
    sum2 = sum(dq2)
    
    if (sum1+sum2) % 2 != 0:
        return -1
    
    for i in range(len(dq1) * 3):
        if sum1 > sum2:
            num = dq1.popleft()
            dq2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            num = dq2.popleft()
            dq1.append(num)
            sum2 -= num
            sum1 += num
        else:
            return i
    
    return -1
