import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
out_space = set([(0,0)])
direcs = [(1,0),(0,1),(-1,0),(0,-1)]
def add_out_space(p: tuple):
    board[p[0]][p[1]] = 0
    out_space.add(p)
    q = deque([p])
    while q:
        y, x = q.popleft()
        for dy, dx in direcs:
            ny, nx = y+dy, x+dx
            if not(0 <= ny < N and 0<= nx < M):
                continue
            np = (ny, nx)
            if board[ny][nx] == 1 or np in out_space:
                continue
            q.append(np)
            out_space.add(np)
add_out_space((0,0))

cheeze = set()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheeze.add((i, j))

result = 0
while cheeze:
    maltings = []
    for key in cheeze:
        cnt = 0
        for dy, dx in direcs:
            np = (key[0]+dy, key[1]+dx)
            if np in out_space:
                cnt += 1
        if cnt >= 2:
            maltings.append(key)
    if maltings:
        result += 1
        for key in maltings:
            cheeze.remove(key)
            add_out_space(key)
print(result)