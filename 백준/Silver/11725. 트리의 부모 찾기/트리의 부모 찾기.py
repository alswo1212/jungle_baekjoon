import sys
from collections import deque
n = int(input())

tree = [[] for _ in range(n+1)]
result = [0] * (n+1)
used = [False] * (n+1)
for _ in range(n - 1):
    p, c = map(int, sys.stdin.readline().split())
    tree[p].append(c)
    tree[c].append(p)

q = deque([1])
while q:
    poped = q.popleft()
    if used[poped] : continue
    used[poped] = True

    for c in tree[poped]:
        q.append(c)
        if result[c] == 0:
            result[c] = poped

print(*result[2:],sep='\n')