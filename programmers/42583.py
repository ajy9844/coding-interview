from collections import deque

def solution(bridge_length, weight, truck_weights):    
    t, w = 1, 0
    trucks = deque(truck_weights)
    bridge = deque()
    
    while trucks:
        if bridge and bridge[0][1] == t:
            truck = bridge.popleft()
            w -= truck[0]
            
        cur = trucks[0]
        if cur + w <= weight:
            truck = trucks.popleft()
            bridge.append([truck, (t+bridge_length)])
            w += truck
        t += 1
    
    return bridge.pop()[1]
