import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(1, K+1):
        if w >= arr[i-1][0]:
            temp = arr[i-1][1] + dp[i-1][w - arr[i-1][0]]
            dp[i][w] =  temp if temp > dp[i-1][w] else dp[i-1][w]
        else:
            dp[i][w] = dp[i-1][w]

print(dp[N][K])