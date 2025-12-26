import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    num = int(input())
    if num == 0:
        print(0 if not hq else heappop(hq))
    else :
        heappush(hq, num)