n = int(input())

W = [list(map(int, input().split())) for _ in range(n)]

is_visit = [False] * n
visit_seq = [-1] * n

result = 1_000_000 * n

def dfs(depth):
    if depth == n : 
        cost_sum = 0
        for i in range(n-1, -1, -1):
            cost = W[visit_seq[i]][visit_seq[i-1]]
            if not cost : return
            cost_sum += cost
            
        global result
        result = min(result, cost_sum)
        return
    
    for i in range(n):
        if is_visit[i] : continue
        if depth != 0 and not W[visit_seq[depth - 1]][i] : continue
        
        is_visit[i] = True
        visit_seq[n-1-depth] = i
        dfs(depth+1)
        visit_seq[n-1-depth] = -1
        is_visit[i] = False

dfs(0)

print(result)