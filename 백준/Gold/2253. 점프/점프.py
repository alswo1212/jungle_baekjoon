import sys
sys.setrecursionlimit(int(1e8))
N, M = map(int, input().split())
ignore = set([int(input()) for _ in range(M)])
MAX = int((2*N) ** 0.5)
memo = [[sys.maxsize] * (MAX + 2) for _ in range(N+1)]

memo[1][0] = 0 # 1 번 돌에서 시작
for i in range(2,N+1): # 2번 돌로 점프를 시작
    if i in ignore:
        continue
    for v in range(1, int((2 * i) ** 0.5) + 1):
        # 해당 속도로 올 수 있는 돌 중에서 가장 작은 횟수 + 1
        memo[i][v] = min(memo[i-v][v-1],memo[i-v][v],memo[i-v][v+1]) + 1

result = min(memo[N])
print(-1 if result == sys.maxsize else result)