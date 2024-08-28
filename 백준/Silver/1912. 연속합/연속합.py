from sys import maxsize
N = int(input())
nums = list(map(int, input().split()))
memo = [-maxsize] * (N+1)

for i in range(1, N+1):
    memo[i] = max(nums[i-1], memo[i-1] + nums[i-1])

print(max(memo))