import sys
input = sys.stdin.readline
n = int(input())
querys = []
memo_len = 0
for _ in range(n):
    querys.append(int(input()))
    if memo_len < querys[-1]:
        memo_len = querys[-1]

memo = [1] * (memo_len + 1)
if memo_len >= 2:
    memo[2] = memo[1] + memo[0]

for i in range(3, len(memo), 1):
    memo[i] = (memo[i-1] + memo[i-2] + memo[i-3]) % 1_000_000_009

for i in range(n):
    querys[i] = memo[querys[i]]

print(*querys, sep='\n')