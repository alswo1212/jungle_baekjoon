import sys
N = int(sys.stdin.readline())
in_out = sys.stdin.readline()
links = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    links[a-1].append(b-1)
    links[b-1].append(a-1)

visit = [False] * N
def dfs(start, now, links, visit, in_out):
    if start != now and in_out[now] == '1':
        return 1
    result = 0
    for next in links[now]:
        if visit[next] : continue
        visit[next] = True
        result += dfs(start, next, links, visit, in_out)
        visit[next] = False
    return result

result = 0
for i in range(N):
    if in_out[i] == '0': continue
    visit[i] = True
    result += dfs(i, i, links, visit, in_out)
    visit[i] = False
print(result)