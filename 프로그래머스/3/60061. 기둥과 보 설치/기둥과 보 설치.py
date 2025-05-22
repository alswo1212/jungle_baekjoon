def solution(n, build_frame):
    answer = []
    N = 2 * n + 4
    board = [[0] * N for _ in range(N)]

    def is_save(r:int, c:int)->bool:
        if board[r+1][c]:
            if not (board[r][c+1] or board[r][c-1]) and not board[r-1][c]:
                return False
        if board[r][c-1]:
            if (not board[r-1][c] and 
                not board[r-1][c-2] and
                not (board[r][c-3] and board[r][c+1])):
                return False
        if board[r][c+1]:
            if (not board[r-1][c] and 
                not board[r-1][c+2] and
                not (board[r][c-1] and board[r][c+3])):
                return False
        return True
    
    for x, y, a, b in build_frame:
        x <<= 1
        x += 2
        y <<= 1
        if a == 0 and b == 1:
            if y == 0 or board[y-1][x] or board[y][x] or board[y][x-1]:
                board[y][x] = 1
                board[y+1][x] = 1
        elif a == 1 and b == 1:
            if (board[y-1][x] or 
                board[y-1][x+2] or 
                (board[y][x-1] and board[y][x+3])):
                board[y][x] = 1
                board[y][x+1] = 1
        elif a == 0 and b == 0:
            if not board[y][x+1]:
                board[y][x] = 0
            board[y+1][x] = 0
            if not is_save(y+2,x):
                board[y][x] = 1
                board[y+1][x] = 1
                
        elif a == 1 and b == 0:
            if not board[y+1][x]:
                board[y][x] = 0
            board[y][x+1] = 0
            if not is_save(y,x+2) or not is_save(y, x):
                board[y][x] = 1
                board[y][x+1] = 1
    
    for j in range(2, N, 2):
        x = (j-2) >> 1
        for i in range(0, N, 2):
            y = i >> 1
            if board[i+1][j]:
                answer.append([x,y,0])
            if board[i][j+1]:
                answer.append([x,y,1])
    
    return answer