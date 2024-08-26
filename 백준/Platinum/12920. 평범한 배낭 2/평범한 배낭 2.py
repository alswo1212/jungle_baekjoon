N, M = map(int, input().split())
arr = []
memo = [0] * (M+1)
for _ in range(N):
    V, C, K = map(int, input().split())

    cnt = 1
    while K > 0:
        temp = cnt if cnt < K else K
        arr.append((V * temp, C * temp))

        K -= cnt
        cnt <<= 1

for weight, value in arr:
    for w in range(M, weight-1, -1):
        memo[w] = max(memo[w], memo[w - weight] + value)

print(memo[M])