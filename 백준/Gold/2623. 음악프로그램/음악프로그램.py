import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
ingreeds = [0] * N
edges = [[] for _ in range(N)]

for _ in range(M):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    for i in range(n-1):
        edges[arr[i+1] - 1].append(arr[i] - 1)
        ingreeds[arr[i] - 1] += 1

q = deque()
for i in range(N):
    if ingreeds[i] == 0:
        q.append(i)

result = [0] * N
result_idx = N-1
while q:
    idx = q.popleft()
    result[result_idx] = idx + 1
    result_idx -= 1
    for i in edges[idx]:
        ingreeds[i] -= 1
        if ingreeds[i] == 0:
            q.append(i)
if q:
    print(0)
else:
    print(*result,sep='\n')