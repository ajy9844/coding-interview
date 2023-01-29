import math

def convert(num, base):
    tmp = ''
    while num:
        num, r = divmod(num, base)
        tmp += str(r)
        
    return tmp[::-1]

def is_prime_number(num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    nums = convert(n, k).split('0')
    nums = list(filter(None, nums))
    
    for num in nums:
        if is_prime_number(int(num)):
            answer += 1
    
    return answer
