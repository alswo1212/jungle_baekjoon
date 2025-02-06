from collections import deque
def solution(maze):
    direc = [(1,0),(0,1),(-1,0),(0,-1)]
    n, m = len(maze), len(maze[0])
    q = deque()
    ends = [None] * 2
    wagon = [[0,0], [0,0]] 
    for i in range(n):
        for j in range(m):
            if 0 < maze[i][j] <= 2:
                wagon[maze[i][j]-1] = (i, j)
            elif 3 <= maze[i][j] <= 4:
                ends[maze[i][j]-3] = (i, j)
    
    red_bit = 1 << (wagon[0][0] * m + wagon[0][1])
    blue_bit = 1 << (wagon[1][0] * m + wagon[1][1])
    
    q.append((tuple(wagon[0]),tuple(wagon[1]), red_bit, blue_bit, 0))
    while q:
        red, blue, rbit, bbit, cnt = q.popleft()
        if red == ends[0] and blue == ends[1]:
            return cnt
        
        if red == ends[0]:
            for dy, dx in direc:
                b_ny, b_nx = blue[0]+dy, blue[1]+dx
                if not (0 <= b_ny < n and 0 <= b_nx < m):
                    continue
                if maze[b_ny][b_nx] == 5:
                    continue
                if 1 << (b_ny * m + b_nx) & bbit:
                    continue
                n_blue = (b_ny, b_nx)
                if red == n_blue:
                    continue
                q.append((red, n_blue, rbit, 1 << (b_ny * m + b_nx) | bbit, cnt+1))
        elif blue == ends[1]:
            for dy, dx in direc:
                r_ny, r_nx = red[0]+dy, red[1]+dx
                if not (0 <= r_ny < n and 0 <= r_nx < m):
                    continue
                if maze[r_ny][r_nx] == 5:
                    continue
                if 1 << (r_ny * m + r_nx) & rbit:
                    continue
                n_red = (r_ny, r_nx)
                if blue == n_red:
                    continue
                q.append((n_red, blue, 1 << (r_ny * m + r_nx) | rbit, bbit, cnt+1))
        else:
            for dy, dx in direc:
                r_ny, r_nx = red[0]+dy, red[1]+dx
                if not (0 <= r_ny < n and 0 <= r_nx < m):
                    continue
                if maze[r_ny][r_nx] == 5:
                    continue
                if 1 << (r_ny * m + r_nx) & rbit:
                    continue
                n_red = (r_ny, r_nx)
                n_rbit = 1 << (r_ny * m + r_nx) | rbit
                for dy2, dx2 in direc:
                    b_ny, b_nx = blue[0]+dy2, blue[1]+dx2
                    if not (0 <= b_ny < n and 0 <= b_nx < m):
                        continue
                    if maze[b_ny][b_nx] == 5:
                        continue
                    if 1 << (b_ny * m + b_nx) & bbit:
                        continue
                    n_blue = (b_ny, b_nx)
                    if (n_blue == red and n_red == blue) or n_blue == n_red:
                        continue
                    n_bbit = 1 << (b_ny * m + b_nx) | bbit
                    q.append((n_red, n_blue, n_rbit, n_bbit, cnt+1))

    return 0