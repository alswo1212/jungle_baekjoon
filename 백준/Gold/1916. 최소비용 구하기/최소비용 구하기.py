import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())

costs = [[sys.maxsize] * N for _ in range(N)]
min_cost = [sys.maxsize] * N
for _ in range(M):
    start, to, cost = map(int, input().split())
    costs[start -1][to - 1] = min(cost, costs[start -1][to - 1])

start, end = map(lambda n : int(n) - 1, input().split())
q = []
heapq.heappush(q, (0, start))

min_cost[start] = 0

while q:
    now_cost, now = heapq.heappop(q)
    
    for i in range(len(costs[now])):
        if i == now : continue
        if costs[now][i] == sys.maxsize :continue
        next_cost = now_cost + costs[now][i]
        if min_cost[i] > next_cost:
            heapq.heappush(q, (next_cost, i))
            min_cost[i] = next_cost

print(min_cost[end])