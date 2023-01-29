from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1
    candidates = list(combinations_with_replacement(range(0, 11), n))        
    
    for candidate in candidates:
        info2 = [0]*11
        apeach, ryan = 0, 0
        
        for score in candidate:
            info2[10-score] += 1
        
        for idx, (a, r) in enumerate(zip(info, info2)):
            if a == r == 0:
                continue
            elif a >= r:
                apeach += (10-idx)
            else:
                ryan += (10-idx)
        
        if ryan > apeach:
            gap = ryan - apeach
            if gap > max_gap:
                max_gap = gap
                answer = info2
    
    return answer
