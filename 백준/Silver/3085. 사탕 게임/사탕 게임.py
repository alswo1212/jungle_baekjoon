import sys
input = sys.stdin.readline

N = int(input())
board = [[*input().strip()] for _ in range(N)]
def check_hor(board:list[str], y:int)->int:
    cnt, temp = 0, 0
    c = board[y][0]
    for i in range(len(board)):
        if c == board[y][i]:
            temp += 1
        else:
            c = board[y][i]
            temp = 1
        if temp > cnt:
            cnt = temp
    return cnt

def check_ver(board:list[str], x:int)->int:
    cnt, temp = 0, 0
    c = board[0][x]
    for i in range(len(board)):
        if c == board[i][x]:
            temp += 1
        else:
            c = board[i][x]
            temp = 1
        if temp > cnt:
            cnt = temp
    return cnt
    
result = 0
for i in range(N):
    result = max(check_hor(board, i), check_ver(board, i), result)
    
# 상우하좌
direc = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(N):
    for j in range(N):
        for y, x in direc:
            ny, nx = i+y, j+x
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if board[i][j] == board[ny][nx]:
                continue

            board[ny][nx], board[i][j] = board[i][j], board[ny][nx]

            result = max(check_hor(board, i), check_ver(board, j), result)
            if ny != i:
                result = max(check_hor(board, ny), result)
            else:
                result = max(check_ver(board, nx), result)
                
            board[ny][nx], board[i][j] = board[i][j], board[ny][nx]

print(result)