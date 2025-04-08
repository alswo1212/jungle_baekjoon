from collections import deque
def solution(n, roads, sources, destination):
    destination -= 1    
    edges = [[] for _ in range(n)]
    for a, b in roads:
        a, b = a-1, b-1
        edges[a].append(b)
        edges[b].append(a)
    
    memo = [-1] * n
    visit = [False] * n
    visit[destination] = True
    q = deque([(destination, 0)])
    while q:
        node, dist = q.popleft()
        memo[node] = dist

        for next_node in edges[node]:
            if visit[next_node]:
                continue
            visit[next_node] = True
            q.append((next_node, dist+1))
    return list(map(lambda n: memo[n-1], sources))