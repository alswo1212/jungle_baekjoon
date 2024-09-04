import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    start, to, time = map(int, input().split())
    edges[start-1].append((to-1, time))
    edges[to-1].append((start-1, time))
    
visit = [False] * N
q = [(0, 0)]
max_time = 0
while q:
    sum_time, start = heappop(q)
    sum_time = -sum_time
    visit[start] = True
    if sum_time > max_time:
        max_time = sum_time
    for next, cost_time in edges[start]:
        if visit[next] : continue
        heappush(q, (-cost_time - sum_time, next))

print(max_time)