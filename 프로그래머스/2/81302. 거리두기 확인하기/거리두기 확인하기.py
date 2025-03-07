from collections import deque
def solution(places):
    direc = [[1,0],[0,1],[-1,0],[0,-1]]
    
    def check_dist(i:int, j:int, board:list)->bool:
        n, m = len(board), len(board[0])
        q = deque([(i,j, 0)])
        visit = set([(i,j)])
        while q:
            y, x, dist = q.popleft()
            if dist == 2:
                continue
            for dy, dx in direc:
                ny, nx = y+dy, x+dx
                if not (0<=ny<n and 0<=nx<m): 
                    continue
                np = (ny, nx)
                if np in visit:
                    continue
                if board[ny][nx] == 'X':
                    continue
                elif board[ny][nx] == 'P':
                    return False
                
                visit.add(np)
                q.append((ny, nx, dist+1))
        return True
    
    def check_board(board:list)->int:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != 'P' :
                    continue
                if not check_dist(i, j, board):
                    return 0
        return 1
            
    return list(map(check_board, places))