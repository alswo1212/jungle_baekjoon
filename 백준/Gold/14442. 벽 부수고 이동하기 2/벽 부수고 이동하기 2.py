import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
direc = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs() -> int:
    visit = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = 1
    q = deque([(0,0,0)])
    while q:
        y, x, k = q.popleft()
        if y == N-1 and x == M-1:
            return visit[-1][-1][k]

        for dy, dx in direc:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M :
                if board[ny][nx] == 0 and visit[ny][nx][k] == 0:
                    visit[ny][nx][k] = visit[y][x][k] + 1
                    q.append((ny, nx, k))
                elif board[ny][nx] == 1 and k < K and visit[ny][nx][k+1] == 0:
                    visit[ny][nx][k+1] = visit[y][x][k] + 1
                    q.append((ny, nx, k+1))
    return -1
            
print(bfs())