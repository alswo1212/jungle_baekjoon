from collections import deque
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: q.append((i,j))

result = 0
direc = [[0,1],[0,-1],[1,0],[-1,0]]
while q:
    y, x = q.popleft()
    days = arr[y][x]
    for dy, dx in direc:
        ny, nx = y+dy, x+dx
        if not(0 <= ny < N and 0 <= nx < M): continue
        if arr[ny][nx] != 0: continue
        arr[ny][nx] = days+1
        result = days
        q.append((ny,nx))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result = -1
            break

print(result)