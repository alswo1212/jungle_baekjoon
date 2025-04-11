from collections import deque
def solution(board):
    N, M = len(board), len(board[0])
    visit = [[False] * M for _ in range(N)]
    q = deque()
    target = None
    direc = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j, 0))
                visit[i][j] = True
            elif board[i][j] == 'G':
                target = (i, j)
    
    while q:
        r, c, cnt = q.popleft()
        if target == (r,c):
            return cnt
        
        for dy, dx in direc:
            nr, nc = r, c
            while 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 'D':
                nr, nc = nr+dy, nc+dx
            nr, nc = nr-dy, nc-dx
            if not visit[nr][nc]:
                visit[nr][nc] = True
                q.append((nr,nc,cnt+1))

    return -1