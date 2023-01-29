def solution(nums):
    n = len(nums)
    k = len(set(nums))
    
    if n//2 > k:
        return k
    else:    
        return n//2
