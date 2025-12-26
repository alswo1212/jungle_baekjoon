import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
ing = []
waiting = []
result = 0
for _ in range(N):
    S, T = map(int, input().split())
    heappush(waiting, (S,T))

while waiting:
    S, T = heappop(waiting)
    while ing and ing[0] <= S:
        heappop(ing)
    heappush(ing, T)
    result = max(result, len(ing))
print(result)