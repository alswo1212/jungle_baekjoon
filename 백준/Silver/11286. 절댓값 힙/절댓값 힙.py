import sys
from heapq import heappush, heappop
input = sys.stdin.readline
hq = []

N = int(input())
result = []
for _ in range(N):
    num = int(input())
    if num == 0:
        result.append(str(0 if not hq else heappop(hq)[1]))
    else:
        heappush(hq, (abs(num), num))

print('\n'.join(result))