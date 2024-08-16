from heapq import heappop, heappush
import sys
heap = []
result = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        result.append(-heappop(heap) if len(heap) else 0)
        continue
    heappush(heap, -num)
    
print(*result,sep='\n')