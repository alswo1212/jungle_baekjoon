from sys import maxsize
N = int(input())
nums = list(map(int, input().split()))
K = int(input())
length = max(nums) * (K + 1)
memo = [maxsize] * length
for i in range(K+1):
    memo[i] = i

for idx in range(1, len(nums)):
    num = nums[idx]
    for k in range(1, K+1):
        mult_num = num * k
        for i in range(len(memo) - 1, 0, -1):
            if i - mult_num >= 0:
                memo[i] = min(memo[i], memo[i-mult_num]+k)

for i in range(len(memo)):
    if memo[i] > K:
        print(f'{"holsoon" if i % 2 == 0 else "jjaksoon"} win at {i}')
        break