import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

memo = [0] * (N+51)
for i in range(N-1, -1, -1):
    if arr[i][0] + i <= N:
        memo[i] = max(memo[i+1], arr[i][1] + memo[i + arr[i][0]])
    else:
        memo[i] = memo[i+1]
print(memo[0])