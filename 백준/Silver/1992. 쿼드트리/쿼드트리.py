import sys
n = int(sys.stdin.readline())
board = [sys.stdin.readline().strip() for _ in range(n)]

def bw_zip(r_idx, c_idx, n, board):
    num = board[r_idx][c_idx]

    for i in range(r_idx, r_idx + n):
        for j in range(c_idx, c_idx + n):
            if num != board[i][j]:
                next_n = n >> 1
                zip1 = bw_zip(r_idx, c_idx,  next_n, board)
                zip2 = bw_zip(r_idx, c_idx + next_n,  next_n, board)
                zip3 = bw_zip(r_idx + next_n, c_idx,  next_n, board)
                zip4 = bw_zip(r_idx + next_n, c_idx + next_n,  next_n, board)
                return f'({zip1}{zip2}{zip3}{zip4})'
    return f'{num}'

print(bw_zip(0,0,n,board))