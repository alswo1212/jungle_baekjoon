import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[]] + [[] for _ in range(N)]
for _ in range(N-1):
    node1, node2, dist = map(int, input().split())
    edges[node1].append((node2, dist))
    edges[node2].append((node1, dist))

def go(start:int, end:int) -> int:
    visit = [False] * (N+1)
    visit[start] = True
    q = deque([(start, 0)])
    while q:
        now, dist = q.popleft()
        if now == end:
            return dist
        for next, next_dist in edges[now]:
            if visit[next]:
                continue
            visit[next] = True
            q.append((next, next_dist + dist))
    
for _ in range(M):
    start, end = map(int, input().split())
    print(go(start, end))
