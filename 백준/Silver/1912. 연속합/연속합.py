from sys import maxsize
N = int(input())
nums = list(map(int, input().split()))
memo = [[-maxsize] * (N+1) for _ in range(2)]

for i in range(1, N+1):
    memo[0][i] = nums[i-1]

for i in range(1, N+1):
    memo[1][i] = max(memo[0][i], memo[1][i-1] + nums[i-1])

print(max(memo[1]))