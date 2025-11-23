import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N, k = map(int, input().split())
len_map = defaultdict(list)

for i in range(N):
    name = input()
    len_map[len(name)].append(i)

q = deque()
result = 0
for indexs in len_map.values():
    for idx in indexs:
        while q and q[0]+k < idx:
            q.popleft()
        result += len(q)
        q.append(idx)
    q.clear()

print(result)