import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

sea = [list(map(int, input().split())) for _ in range(N)]
q = deque()
stack = []
direc = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(N):
    for j in range(M):
        if sea[i][j] != 0:
            q.append([i,j, sea[i][j]])

def check(visit, q):
    for item in q:
        y, x, _ = item
        visit[y][x] = True

    temp_q = deque([[y,x]])
    while temp_q:
        y, x = temp_q.popleft()
        for d in direc:
            ny = y + d[0]
            nx = x + d[1]
            if not(0 <= ny < N): continue
            if not(0 <= nx < M): continue
            if visit[ny][nx]:
                visit[ny][nx] = False
                temp_q.append([ny,nx])
    
    for item in q:
        y, x, _ = item
        if visit[y][x]: return True
        visit[y][x] = False
    return False

visit = [[False] * M for _ in range(N)]
day = 0
while q:
    mellting = []
    for _ in range(len(q)):
        y, x, c = q.popleft()
        cnt = 0
        for d in direc:
            ny = y + d[0]
            nx = x + d[1]
            if not(0 <= ny < N): continue
            if not(0 <= nx < M): continue
            if sea[ny][nx] == 0:
                cnt += 1
        c -= cnt
        if c <= 0:
            mellting.append([y,x])
        else:
            sea[y][x] = c
            q.append([y,x,c])

    for y,x in mellting:
        sea[y][x] = 0

    day += 1
    if not q:
        print(0)
        break

    if check(visit, q):
        print(day)
        break
