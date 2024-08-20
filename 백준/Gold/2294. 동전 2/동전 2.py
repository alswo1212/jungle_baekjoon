import sys
import heapq
input = sys.stdin.readline

n, k = map(int,input().split())
coins = set()
for _ in range(n):
    coins.add(int(input()))
coins = list(coins)
q = []
heapq.heappush(q, (0, k))
visit = [False] * (k+1)

result = -1
while q:
    cnt, target = heapq.heappop(q)
    if target == 0:
        result = cnt
        break

    for coin in coins:
        next_target = target - coin
        if next_target < 0 or visit[next_target]: continue
        visit[next_target] = True
        heapq.heappush(q, (cnt+1, next_target))

print(result)