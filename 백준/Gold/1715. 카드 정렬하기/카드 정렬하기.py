import heapq
import sys
heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

result = 0
while len(heap) > 1:
    temp = heapq.heappop(heap) + heapq.heappop(heap)
    result += temp
    heapq.heappush(heap, temp)

print(result)