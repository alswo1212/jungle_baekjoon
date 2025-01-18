import sys
input = sys.stdin.readline

N, K = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

hq = [(0, K, 1 << K)]
goal = (1 << N) - 1

def solv(time:int, planet:int, visits:int) -> int:
    if visits == goal:
        return time
    result = float('inf')

    for i in range(N):
        temp_visit = (1 << i) | visits
        if temp_visit == visits:
            continue
        result = min(result, solv(time + edges[planet][i], i, temp_visit))
    return result

print(solv(0, K, 1 << K))