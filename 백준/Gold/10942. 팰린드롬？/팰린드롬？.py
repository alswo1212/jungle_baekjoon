import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
SE = [list(map(int, input().split())) for _ in range(M)]

dp = [[False] * N for _ in range(N)]

for length in range(N):
    for start in range(N - length):
        end = start + length
        if end == start :
            dp[start][end] = True
        elif arr[start] == arr[end]:
            if start + 1 == end:
                dp[start][end] = True
            elif dp[start+1][end-1] : 
                dp[start][end] = True

for S, E in SE:
    print(1 if dp[S-1][E-1] else 0)