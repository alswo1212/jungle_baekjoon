import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
q = []
inputs = [list(map(int,input().split())) for _ in range(N)]
for item in inputs:
    heappush(q, item)

min_val = sys.maxsize
while q:
    go_time, pay_time = heappop(q)
    if go_time > pay_time : continue
    if pay_time < min_val:
        min_val = pay_time
    else : 
        break

print(-1 if min_val == sys.maxsize else min_val)