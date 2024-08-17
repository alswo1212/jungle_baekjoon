import sys
from collections import deque
n = int(sys.stdin.readline())
visit = [False] * n
net = [[] for _ in range(n)]

for _ in range(int(sys.stdin.readline())):
    a,b = map(lambda s: int(s) - 1, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)

q = deque([0])
result = 0
while q:
    poped = q.popleft()
    if visit[poped]: continue

    visit[poped] = True
    result += 1
    q.extend(net[poped])

print(result - 1)