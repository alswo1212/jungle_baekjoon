import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, M): dp[0][i] += dp[0][i-1]

for i in range(1, N):
    l2r_temp = dp[i][:]
    r2l_temp = dp[i][:]

    for j in range(M):
        l2r_temp[j] += dp[i-1][j] if j == 0 else max(dp[i-1][j], l2r_temp[j-1])

    for j in range(M-1, -1, -1):
        r2l_temp[j] += dp[i-1][j] if j == M-1 else max(dp[i-1][j], r2l_temp[j+1])
    
    for j in range(M):
        dp[i][j] =  l2r_temp[j] if l2r_temp[j] > r2l_temp[j] else r2l_temp[j]

print(dp[N-1][M-1])