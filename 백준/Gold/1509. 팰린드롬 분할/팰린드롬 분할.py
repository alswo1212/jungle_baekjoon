import sys
input = sys.stdin.readline

string = input().strip()
N = len(string)

dp = [2500 for _ in range(N + 1)]
dp[-1] = 0
is_p = [[False] * N for i in range(N)]

for i in range(N): is_p[i][i] = True
for i in range(1, N):
    if string[i - 1] == string[i]:
        is_p[i - 1][i] = True

for length in range(3, N + 1):
    for start in range(N + 1 - length):
        end = start + length - 1
        if string[start] == string[end] and is_p[start + 1][end - 1]:
            is_p[start][end] = True

for end in range(N):
    for start in range(end + 1):
        idx = (start if is_p[start][end] else end) - 1
        dp[end] = min(dp[end], dp[idx] + 1)

print(dp[N - 1])