import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
lines = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    lines.append((min(a,b), max(a,b)))
lines.sort()
L = int(sys.stdin.readline())
heap = []

max_cnt = 0
for i in range(len(lines)-1, -1, -1):
    start, end = lines[i]
    if end - start > L: continue

    heappush(heap, -end)

    while heap and -heap[0] > start + L:
        heappop(heap)

    max_cnt = max(max_cnt, len(heap))
print(max_cnt)