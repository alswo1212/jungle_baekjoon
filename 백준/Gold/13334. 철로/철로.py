import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
lines = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    lines.append((min(a,b), max(a,b)))
lines.sort(key=lambda l : l[1])

L = int(sys.stdin.readline())
heap = []

max_cnt = 0
for line in lines:
    if line[1] - line[0] > L: continue

    while heap and heap[0] < line[1] - L:
        heappop(heap)

    heappush(heap, line[0])
    max_cnt = max(max_cnt, len(heap))
print(max_cnt)