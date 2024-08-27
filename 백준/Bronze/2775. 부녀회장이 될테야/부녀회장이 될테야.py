import sys
input = sys.stdin.readline
memo = [[0] * 15 for _ in range(15)]
for i in range(1, 15): memo[0][i] = i

for i in range(1, 15):
    for j in range(1,15):
        memo[i][j] = memo[i][j-1] + memo[i-1][j]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(memo[k][n])