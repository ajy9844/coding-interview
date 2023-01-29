from itertools import product
import bisect

def get_groups(str):
    groups = []
    lst = str.split(' ')
    iter = [['-'] for _ in range(4)]
    
    for i, item in enumerate(lst):
        iter[i].append(item)
    for tup in product(iter[0], iter[1], iter[2], iter[3]):
        groups.append(' '.join(tup))
    
    return groups

def solution(infos, query):
    answer = []
    groups = {}
    
    iter1 = ['cpp', 'java', 'python', '-']
    iter2 = ['backend', 'frontend', '-']
    iter3 = ['junior', 'senior', '-']
    iter4 = ['chicken', 'pizza', '-']
    
    for tup in product(iter1, iter2, iter3, iter4):
        group = ' '.join(tup)
        groups[group] = []
        
    for info in infos:
        i = info.rfind(' ')
        input, score = info[:i], int(info[i+1:])
        for group in get_groups(input):
            bisect.insort(groups[group], score)
    
    for q in query:
        lst = q.split(' ')
        lst = [item for item in lst if item != 'and']
        x = int(lst.pop())
        
        scores = groups[' '.join(lst)]
        num = len(scores) - bisect.bisect_left(scores, x)
        answer.append(num) 

    return answer
