import collections

def solution(participant, completion):
    dict = collections.Counter(participant)
    
    for x in completion:
        if dict[x] > 1:
            dict[x] -= 1
        else:
            del(dict[x])
    
    return list(dict.keys())[0]
