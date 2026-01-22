import sys
from collections import deque
input = sys.stdin.readline

def bfs(board:list[list[int]]) -> int:
    q = deque()
    cnt = 0
    direc = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1),]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0: continue
            q.append((i,j))
            board[i][j] = 0
            cnt += 1
            while q:
                y, x = q.popleft()

                for dx, dy in direc:
                    nx, ny = x+dx, y+dy
                    if not (0 <= ny < len(board) and 0 <= nx < len(board[ny])):
                        continue
                    if board[ny][nx] == 0:
                        continue
                    board[ny][nx] = 0
                    q.append((ny,nx))
    return cnt

result = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    result.append(bfs(board))

print(*result, sep='\n')