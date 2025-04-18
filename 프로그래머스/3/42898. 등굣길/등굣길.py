def solution(m, n, puddles):
    board = [[0]*m for _ in range(n)]
    ignore = [[False]*m for _ in range(n)]
    for x, y in puddles:
        ignore[y-1][x-1] = True
    board[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i+1 < n and not ignore[i+1][j]:
                board[i+1][j] = (board[i][j] + board[i+1][j]) % 1_000_000_007
            if j+1 < m and not ignore[i][j+1]:
                board[i][j+1] = (board[i][j] + board[i][j+1]) % 1_000_000_007
    
    return board[-1][-1]