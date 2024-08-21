from collections import deque
direc = [(1,0),(-1,0),(0,1),(0,-1)]
N = int(input())
board = [input().strip() for _ in range(N)]
visit = [[False] * N for _ in range(N)]

def BFS(y,x, board):
    q = deque([[y,x]])
    visit[y][x] = True
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for d in direc:
            ny, nx = r + d[0], c + d[1]
            if not 0 <= ny < N : continue
            if not 0 <= nx < N : continue
            if visit[ny][nx]: continue
            if board[ny][nx] == '0': continue
            visit[ny][nx] = True
            q.append([ny,nx])
    return cnt

result = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and not visit[i][j]:
            result.append(BFS(i,j,board))

print(len(result))
result.sort()
print(*result, sep='\n')