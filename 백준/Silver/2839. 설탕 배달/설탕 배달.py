import sys
N = int(input())
memo = [sys.maxsize] * (N+1)
memo[0] = 0
weights = [3,5]

for w in weights:
    for i in range(w, N+1):
        memo[i] = min(memo[i-w] + 1, memo[i])

print(-1 if memo[N] == sys.maxsize else memo[N])