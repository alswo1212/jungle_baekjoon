import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, K = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

hq = [(0, K, 1 << K)]
goal = (1 << N) - 1

while hq:
    time, planet, visits = heappop(hq)
    if visits == goal:
        print(time)
        break
    for next_planet in range(N):
        temp_visit = visits | (1 << next_planet)
        if temp_visit == visits:
            continue
        data = (edges[planet][next_planet] + time, next_planet, temp_visit)
        heappush(hq, data)