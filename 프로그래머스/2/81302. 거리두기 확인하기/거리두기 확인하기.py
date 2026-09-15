from collections import deque

def solution(places:list[list[str]]):
    def bfs(board:list[str]):
        directs = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = set()
        q = deque()
        for i in range(len(board)):
            for j in range(len(board[i])):
                visit.clear()
                now = (i,j)
                if board[i][j] == 'P':
                    q.append((i,j,2))
                    visit.add(now)
                
                while q:
                    row, col, rest = q.popleft()
                    if rest == 0: continue
                    for dy, dx in directs:
                        ny, nx = dy+row, dx+col
                        if not (0 <= ny < len(board) and 0 <= nx < len(board[ny])): continue
                        n_point = (ny, nx)
                        if n_point in visit: continue
                        if board[ny][nx] == 'P': return 0
                        if board[ny][nx] == 'X': continue
                        visit.add(n_point)
                        q.append((ny, nx, rest-1))
        return 1
    
    return list(map(bfs, places))