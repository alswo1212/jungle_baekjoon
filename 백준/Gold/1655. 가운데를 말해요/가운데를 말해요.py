import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
left_heap = [] # 작은것들의 최대힙
right_heap = [] # 큰것들의 최소힙
result = []
for _ in range(n):
    num = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heappush(left_heap, -num)
    else:
        heappush(right_heap, num)
    
    if right_heap and right_heap[0] < -left_heap[0]:
        right_pop = heappop(right_heap)
        left_pop = -heappop(left_heap)

        heappush(left_heap, -right_pop)
        heappush(right_heap, left_pop)
    result.append(-left_heap[0])

print(*result, sep='\n')
