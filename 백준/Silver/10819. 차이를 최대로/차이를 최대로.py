n = int(input())

inputs = list(map(int, input().split()))
visit = [False] * n
temp = [0] * n
result = 0

def make_sum(arr):
    return sum([abs(arr[i-1] - arr[i]) for i in range(1, n)])

def dfs(depth):
    if depth == n :
        global result
        result = max(make_sum(temp), result)
        return
    
    for i in range(n):
        if visit[i] : continue

        visit[i] = True
        temp[depth] = inputs[i]
        dfs(depth + 1)
        visit[i] = False

dfs(0)
print(result)