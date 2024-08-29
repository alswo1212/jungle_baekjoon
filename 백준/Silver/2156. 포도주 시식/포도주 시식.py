import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
memo = [0] * (N+1) + [0] * 2
memo[1] = nums[0]
if N >= 2:
    memo[2] = memo[1] + nums[1]
if N >= 3:
    for i in range(3, N+1):
        memo[i] = max(memo[i-1], memo[i-2] + nums[i-1], memo[i-3] + nums[i-2] + nums[i-1])

print(max(memo))