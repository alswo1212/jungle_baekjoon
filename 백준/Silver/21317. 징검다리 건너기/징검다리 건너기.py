N = int(input())
needs = [[0,0]] + [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())

# 0[] 작은 점프만
# 1[] 중간 점프 섞음
# 2[] 큰 점프 섞음
memo = [[float('inf')] * N for _ in range(3)]
memo[0][0] = memo[1][0] = memo[2][0] = 0

for i in range(1, N):
    memo[0][i] = memo[0][i-1] + needs[i][0]
for i in range(2, N, 1):
    memo[1][i] = min(
        memo[0][i-1] + needs[i][0],
        memo[0][i-2] + needs[i-1][1],
        memo[1][i-1] + needs[i][0],
        memo[1][i-2] + needs[i-1][1],
        )
for i in range(3, N, 1):
    memo[2][i] = min(
        memo[0][i-1] + needs[i][0],
        memo[0][i-2] + needs[i-1][1],
        memo[1][i-1] + needs[i][0],
        memo[1][i-2] + needs[i-1][1],
        memo[2][i-1] + needs[i][0],
        memo[2][i-2] + needs[i-1][1],
        memo[1][i-3] + K,
        memo[0][i-3] + K,
        )

print(min(memo[0][-1], memo[1][-1], memo[2][-1]))