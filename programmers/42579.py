def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    
    for g, e in zip(genres, enumerate(plays)):
        d[g].append(e)
    
    genre_sort = sorted(list(d.keys()), key=lambda x: -sum(map(lambda y: y[1], d[x])))
    
    for g in genre_sort:
        temp = [e[0] for e in sorted(d[g], key=lambda x: (-x[1], x[0]))]
        answer += temp[:min(len(temp), 2)]
                            
    return answer
