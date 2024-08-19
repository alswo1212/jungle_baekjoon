import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())
M = int(input())

edges = [[] for _ in range(N)]
result = [0] * N
cnts = [0] * N
reduce = [0] * N
for _ in range(M):
    X, Y, Z = map(int, input().split())
    edges[X-1].append((Y-1, Z))
    cnts[Y-1] += 1

reduce[N-1] = 1
q = deque([N-1]) 
while q:
    now = q.popleft()
    
    for next, n_cnt in edges[now]:
        cnts[next] -= 1
        if cnts[next] == 0:
            q.append(next)
        reduce[next] += reduce[now] * n_cnt
    if not edges[now]:
        result[now] = reduce[now]

for i in range(N):
    if not edges[i]:
        sys.stdout.write(f'{i + 1} {result[i]}\n')