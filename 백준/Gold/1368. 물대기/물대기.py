import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
costs = []
edges = []
q = []
for i in range(n):
    cost = int(input())
    costs.append(cost)
    heappush(q, [cost, i])

for _ in range(n):
    edges.append(list(map(int, input().split())))

result = [sys.maxsize] * n
visit = [False] * n

while q:
    cost, idx = heappop(q)
    if visit[idx] : continue
    if result[idx] > cost:
        result[idx] = cost
        visit[idx] = True
    for i in range(n):
        if i == idx : continue
        if visit[i]: continue
        heappush(q, [costs[i], i])
        heappush(q, [edges[idx][i], i])

print(sum(result))