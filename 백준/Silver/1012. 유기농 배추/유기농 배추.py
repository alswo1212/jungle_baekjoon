import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

direc = [(1,0),(-1,0),(0,-1),(0,1),]

result = []
for _ in range(T):
    M, N, K = map(int, input().split())
    bat = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]

    for __ in range(K):
        x, y = map(int, input().split())
        bat[y][x] = 1

    q = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and bat[i][j] == 1:
                q.append([i,j])
                while q:
                    r, c = q.popleft()
                    for d in direc:
                        ny, nx = r + d[0], c + d[1]
                        if not 0 <= ny < N: continue
                        if not 0 <= nx < M: continue
                        if visit[ny][nx]: continue
                        if bat[ny][nx] != 1: continue

                        visit[ny][nx] = True
                        q.append([ny,nx])
                cnt += 1
    
    result.append(cnt)

print(*result,sep='\n')