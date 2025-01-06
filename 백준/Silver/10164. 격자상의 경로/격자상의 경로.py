N, M, K = map(int, input().split())

def go(start:list, end:list, board:list):
    for i in range(start[0]+1, end[0] + 1):
        board[i][start[1]] = board[start[0]][start[1]]
    for i in range(start[1]+1, end[1] + 1):
        board[start[0]][i] = board[start[0]][start[1]]
    
    for i in range(start[0]+1, end[0]+1):
        for j in range(start[1]+1, end[1]+1):
            board[i][j] = board[i-1][j] + board[i][j-1]

board = [[0] * M for _ in range(N)]
board[0][0] = 1
now = [0, 0]
if K != 0:
    goal = [(K-1) // M, (K-1) % M]
    go(now, goal, board)
    now = goal

goal = [N-1, M-1]
go(now, goal, board)
print(board[N-1][M-1])