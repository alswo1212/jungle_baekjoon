from collections import deque
def solution(board):
    n = len(board)
    q = deque([(0,0,0,1,0)])
    visit = set([(0,0,0,1)])
    direc = [(-1,0),(1,0),(0,-1),(0,1)]
    turns = [
        [(1,1,0,0),(-1,1,0,0),(0,0,-1,-1),(0,0,1,-1)],
        [(1,1,0,0),(1,-1,0,0),(0,0,-1,-1),(0,0,-1,1)]
        ]
    while q:
        y1, x1, y2, x2, cnt = q.popleft()
        if y1 == x1 == n-1 or y2 == x2 == n-1:
            return cnt
        
        for dy, dx in direc:
            ny1, nx1 = y1+dy, x1+dx
            ny2, nx2 = y2+dy, x2+dx
            if not (0 <= ny1 < n and 0 <= nx1 < n) : continue
            if not (0 <= ny2 < n and 0 <= nx2 < n) : continue
            if board[ny1][nx1] or board[ny2][nx2] : continue
            position = (ny1, nx1, ny2, nx2)
            if position in visit : continue
            visit.add(position)
            q.append((*position, cnt+1))
        
        idx = 0 if y1 == y2 else 1
        for i in range(len(turns[idx])):
            dy1, dx1, dy2, dx2 = turns[idx][i]
            ny1, nx1 = y1+dy1, x1+dx1
            ny2, nx2 = y2+dy2, x2+dx2
            if not (0 <= ny1 < n and 0 <= nx1 < n) : continue
            if not (0 <= ny2 < n and 0 <= nx2 < n) : continue
            if board[ny1][x1] or board[ny2][x2] or board[y1][nx1] or board[y2][nx2] : continue
            if board[ny1][nx1] or board[ny2][nx2] : continue
            position = (*min((ny1, nx1), (ny2, nx2)), *max((ny1, nx1), (ny2, nx2)))
            if position in visit : continue
            visit.add(position)
            q.append((*position, cnt+1))

    return -1