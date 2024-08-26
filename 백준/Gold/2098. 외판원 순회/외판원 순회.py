import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

def go(now, visit, N, costs, memo):

    if visit == (1 << N) - 1:
        if costs[now][0]:
            return costs[now][0]
        else:
            return sys.maxsize
    
    if (now, visit) in memo: return memo[(now, visit)]

    min_cost = sys.maxsize
    for next in range(1, N):
        if costs[now][next] == 0: continue
        if visit & (1 << next) : continue

        min_cost = min(go(next, visit | (1 << next), N, costs, memo) + costs[now][next], min_cost)
    
    memo[(now, visit)] = min_cost
    return min_cost

print(go(0, 1, N, costs, {}))