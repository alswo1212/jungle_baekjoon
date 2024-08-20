import sys
import heapq
input = sys.stdin.readline
N = int(input())
link = [[] for _ in range(N)]
cnts = [0] * (N)
for i in range(N):
    temp = input().strip()
    for j in range(N):
        if temp[j] == '1':
            cnts[i] += 1
            link[j].append(i)

q = []

for i in range(N):
    if cnts[i] == 0:
        heapq.heappush(q, -i)

result = [0] * N
numbering = N
while q:
    now = -heapq.heappop(q)
    result[now] = numbering
    numbering -= 1

    for i in link[now]:
        cnts[i] -= 1
        if cnts[i] == 0:
            heapq.heappush(q, -i)

if numbering != 0:
    print(-1)
else:
    print(*result)