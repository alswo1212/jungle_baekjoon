import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    deadline, cup = map(int, input().split())
    arr.append((deadline, cup))
arr.sort()

q = []
for deadline, cup in arr:
    heappush(q, cup)
    if deadline < len(q):
        heappop(q)
print(sum(q))