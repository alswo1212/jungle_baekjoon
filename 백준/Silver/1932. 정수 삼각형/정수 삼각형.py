import sys
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(nums[i])):
        if j == 0:
            nums[i][j] += nums[i-1][j]
        elif len(nums[i-1]) == j:
            nums[i][j] += nums[i-1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])

print(max(nums[N-1]))