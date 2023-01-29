def dfs(cur, sheep, wolf, possible):
    global answer, g_info, graph
    if g_info[cur] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1
    
    if sheep <= wolf:
        return
    
    _possible = possible.copy()
    _possible += graph[cur]
    
    for node in _possible:
        dfs(node, sheep, wolf, [x for x in _possible if x != node])

def solution(info, edges):
    global answer, g_info, graph
    answer = 0
    g_info = info
    
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)
    
    dfs(0, 0, 0, [])
    
    return answer
