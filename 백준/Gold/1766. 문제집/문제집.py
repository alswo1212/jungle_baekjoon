from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ingreeds = [0] * N
edges = [[] for _ in range(N)]

for _ in range(M):
    easy, next = map(lambda n: int(n) - 1, input().split())
    edges[easy].append(next)
    ingreeds[next] += 1

q = []
for i in range(N):
    if ingreeds[i] == 0:
        heappush(q, i)

result = [0] * N
index = 0
while q:
    i = heappop(q)
    result[index] = i+1
    index += 1
    for e in edges[i]:
        ingreeds[e] -= 1
        if ingreeds[e] == 0:
            heappush(q, e)
print(*result)