def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    def get_remove_items()->set:
        result = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '':
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    result.add((i,j))
                    result.add((i+1,j))
                    result.add((i,j+1))
                    result.add((i+1,j+1))
        return result
    
    remove_items = get_remove_items()
    while remove_items:
        answer += len(remove_items)
        for i, j in remove_items:
            board[i][j] = ''
        
        for j in range(n):
            top, bottom = m-1, m-1
            while top >= 0:
                if board[bottom][j] == board[top][j] == '':
                    top -= 1
                elif board[bottom][j] != '' and board[top][j] != '':
                    top -= 1
                    bottom -= 1
                else:
                    board[bottom][j], board[top][j] = board[top][j], board[bottom][j]
                    top -= 1
                    bottom -= 1
        remove_items = get_remove_items()
        
    return answer