def solution(n, s, a, b, fares):
    board = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
    for c, d, f in fares:
        c, d = c-1, d-1
        board[c][d] = f
        board[d][c] = f

    s, a, b = s-1, a-1, b-1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]
                    
    return min(board[s][i] + board[a][i] + board[b][i] for i in range(n))