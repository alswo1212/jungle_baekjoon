import sys
input = sys.stdin.readline

S = input().strip()
n = int(input())
A = [input().strip() for _ in range(n)]

dp = [0] * (len(S) + 1)
dp[0] = 1
for i in range(1, len(S) + 1):
    for a in A:
        a_len = len(a)
        if dp[i-a_len] and i >= a_len and S[i-a_len:i] == a:
            dp[i] = 1

print(dp[len(S)])