import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, [*sys.stdin.readline().strip()])) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
q = deque([[0,0]])
visit[0][0] = True
# 상 하 좌 우
dx = [0, 0 ,-1, 1]
dy = [1, -1, 0, 0]
while q:
    poped = q.popleft()

    for i in range(4):
        new_x = poped[1] + dx[i]
        new_y = poped[0] + dy[i]

        if (new_x < 0 or new_x >= M
        or new_y < 0 or new_y >= N):
            continue
        if board[new_y][new_x] == 0: continue
        if visit[new_y][new_x] : continue
        q.append([new_y, new_x])
        visit[new_y][new_x] = True
        board[new_y][new_x] += board[poped[0]][poped[1]]

print(board[N-1][M-1])