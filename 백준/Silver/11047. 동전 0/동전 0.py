import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums = list(filter(lambda n : n <= K, nums))
cnt = 0
for i in range(len(nums) - 1, -1, -1):
    temp =  K // nums[i]
    cnt += temp
    K %= nums[i]
    if K == 0:
        break
print(cnt)