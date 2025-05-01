from heapq import heappush, heappop
from collections import defaultdict
def solution(n, edge):
    answer = 0
    max_len = 0
    edges = defaultdict(set)
    for s, e in edge:
        edges[s].add(e)
        edges[e].add(s)
    q = [(0,1)]
    visit = [False] * (n+1)
    visit[1] = True

    while q:
        dist, node = heappop(q)
        if dist > max_len:
            max_len = dist
            answer = 1
        elif dist == max_len:
            answer += 1
        
        for next_node in edges[node].copy():
            if visit[next_node]:
                continue
            visit[next_node] = True
            heappush(q, (dist+1, next_node))

    return answer