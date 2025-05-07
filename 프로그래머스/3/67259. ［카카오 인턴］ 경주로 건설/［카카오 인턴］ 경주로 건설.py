from collections import deque
def solution(board):
    n = len(board)
    memo = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    direcs = [(1,0),(-1,0),(0,1),(0,-1)] # up, down, right, left
    memo[0][0] = [0,0,0,0]
    out_2_in = [1,0,3,2]

    q = deque([(0,0,-1)])
    while q:
        r, c, d = q.popleft()

        for i, direc in enumerate(direcs):
            nr, nc = r+direc[0], c+direc[1]
            if not (0 <= nr < n and 0 <= nc < n): continue
            if board[nr][nc] == 1: continue

            temp = 0 if d == -1 else memo[r][c][d]
            if d == -1:
                temp += 100
            elif d // 2 == i // 2:
                temp += 100
            else:
                temp += 600
            
            if temp < memo[nr][nc][out_2_in[i]]:
                memo[nr][nc][out_2_in[i]] = temp
                q.append((nr, nc, out_2_in[i]))
    
    return min(memo[-1][-1])