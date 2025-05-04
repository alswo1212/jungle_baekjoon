from collections import defaultdict
from heapq import heappop, heappush
def solution(n, costs):
    answer = 0
    visit = [False] * (n+1)
    edges = defaultdict(list)
    start_node = -1
    min_cost = float('inf')
    for s, e, cost in costs:
        edges[s].append((e,cost))
        edges[e].append((s,cost))
        if cost < min_cost:
            min_cost = cost
            start_node = s
    
    hq = [(0, start_node)]
    while hq:
        cost, node = heappop(hq)
        if visit[node]:
            continue
        visit[node] = True
        answer += cost

        for next_node, need_cost in edges[node]:
            if visit[next_node]:
                continue
            heappush(hq, (need_cost, next_node))
    
    return answer