import sys
from heapq import heappush
input = sys.stdin.readline
cnts = {}

N = int(input())
for _ in range(N):
    num = int(input())
    if num not in cnts:
        cnts[num] = 0
    cnts[num] += 1

q = []
for num, cnt in cnts.items():
    heappush(q, (-cnt, num))

print(q[0][1])