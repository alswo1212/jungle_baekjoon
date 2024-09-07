import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    input()
    nums = list(map(int, input().split()))
    heapify(nums)
    result = 0
    while len(nums) != 1:
        temp = heappop(nums) + heappop(nums)
        result += temp
        heappush(nums, temp)
    print(result)
