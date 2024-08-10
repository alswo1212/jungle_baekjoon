n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]

is_visit = [False] * n
result = 1_000_000 * n

def dfs(start, now, cost_sum, depth):
    if depth == n - 1 : 
        if W[now][start] != 0:
            global result
            result = min(result, cost_sum + W[now][start])
        return

    for next in range(n):
        if is_visit[next] : continue
        if not W[now][next] : continue
        if cost_sum + W[now][next] > result : continue

        is_visit[next] = True
        dfs(start, next, cost_sum+W[now][next], depth+1)
        is_visit[next] = False

for i in range(n): 
    is_visit[i] = True
    dfs(i, i, 0, 0)
    is_visit[i] = False

print(result)