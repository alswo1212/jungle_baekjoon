import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)] + [0] * 4
memo = [0] * (N+5)
memo[1] = nums[0]
memo[2] = nums[0] + nums[1]
memo[3] = max(nums[0] + nums[2], nums[1] + nums[2])
def go_back(n:int):
    if n != 0 and  memo[n] != 0:
        return memo[n]
    if n == 0:
        return 0
    
    memo[n] = max(go_back(n-3) + nums[n-2], go_back(n-2)) + nums[n-1]
    return memo[n]
go_back(N)

print(memo[N])