from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 # ex. (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc
    return answer
