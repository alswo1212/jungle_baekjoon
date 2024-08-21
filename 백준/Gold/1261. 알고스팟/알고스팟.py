import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
miro = [list(input().strip()) for _ in range(N)]
q = deque()

direc = [(1,0),(-1,0),(0,1),(0,-1)]
q.append([0,0])
cnt = 0
visit = [[False] * M for _ in range(N)]
visit[0][0] = True
while q:
    temp = []
    while q:
        y, x = q.popleft()
        if y == N-1 and x == M-1:
            print(cnt)
            quit()
        for d in direc:
            ny, nx = y + d[0], x + d[1]
            if not 0 <= ny < N: continue
            if not 0 <= nx < M: continue
            if visit[ny][nx]: continue

            visit[ny][nx] = True
            if miro[ny][nx] == '1':
                miro[ny][nx] = '0'
                temp.append([ny,nx])
            else:
                q.append([ny,nx])

    q.extend(temp)
    cnt += 1
print(cnt)