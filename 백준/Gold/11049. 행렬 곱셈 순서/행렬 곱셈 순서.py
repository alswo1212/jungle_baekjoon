import sys
input = sys.stdin.readline

N = int(input())
RCs = [list(map(int, input().split())) for _ in range(N)]

memo = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    memo[i][i] = 0

for i in range(1, N):
    memo[i-1][i] = RCs[i-1][0] * RCs[i-1][1] * RCs[i][1]

for i in range(2, N):
    for j in range(N - i):
        for k in range(j, j+i):
            memo[j][j+i] = min(memo[j][j+i], memo[j][k] + memo[k+1][j+i] + RCs[j][0] * RCs[k][1] * RCs[j+i][1])

print(memo[0][N-1])