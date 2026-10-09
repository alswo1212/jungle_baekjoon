def solution(m, n, board):
    answer = 0
    metric = [[*cs] for cs in board]
    check_board = [[False] * n for _ in range(m)]
    
    while True:
        is_match = False
        for i in range(m-1):
            for j in range(n-1):
                if metric[i][j] and metric[i][j] == metric[i+1][j] == metric[i][j+1] == metric[i+1][j+1]:
                    check_board[i][j] = True
                    check_board[i+1][j] = True
                    check_board[i][j+1] = True
                    check_board[i+1][j+1] = True
                    is_match = True
        if not is_match: break
        
        for i in range(m):
            for j in range(n):
                if check_board[i][j]:
                    metric[i][j] = ''
                    answer += 1
                    check_board[i][j] = False
        
        for j in range(n):
            for i in range(m-1, -1, -1):
                if metric[i][j] == '':
                    all_swaped = True
                    for k in range(i-1, -1, -1):
                        if metric[k][j]:
                            all_swaped = False
                            metric[i][j], metric[k][j] = metric[k][j], metric[i][j]
                            break
                    if all_swaped: 
                        break
                
    return answer