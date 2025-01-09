import sys
from collections import deque
input = sys.stdin.readline

def check_num_position(board:list, row:int, col:int) -> bool:
    for i in range(row):
        for j in range(col):
            num = board[i][j]
            for k in range(max(0, i-num), min(i+num+1, row)):
                if board[k][j] == num and k != i:
                    return False
            for k in range(max(0, j-num), min(j+num+1, col)):
                if board[i][k] == num and k != j:
                    return False
    return True

direc = [[-1,0],[0,1],[1,0],[0,-1]]
def check_polynomio(board:list, descrs:list, row:int, col:int) -> bool:
    visit = set()
    q = deque([])
    
    for i in range(row):
        for j in range(col):
            point = (i,j)
            if point in visit:
                continue

            polynomio = [board[i][j]]
            visit.add(point)
            q.append(point)
            while q:
                y, x = q.popleft()
                descr = descrs[y][x]
                for dy, dx in direc:
                    if descr == 0:
                        break
                    if descr % 2 == 1:
                        ny, nx = y+dy, x+dx
                        if not (0 <= ny < row and 0 <= nx < col):
                            descr >>= 1
                            continue
                        new_point = (ny, nx)
                        if new_point in visit:
                            descr >>= 1
                            continue
                        visit.add(new_point)
                        q.append(new_point)
                        polynomio.append(board[new_point[0]][new_point[1]])
                    descr >>= 1
            
            polynomio.sort()
            for k in range(len(polynomio)):
                if k == 0 :
                    if polynomio[k] != 1:
                        return False
                elif polynomio[k] - polynomio[k-1] != 1:
                    return False
            
    return len(visit) == row * col

T = int(input())
result = [0] * T

for t in range(T):
    R, C = map(int, input().split())
    board = [list(map(int, [*input().strip()])) for _ in range(R)]
    descrs = [list(map(int, input().split())) for _ in range(R)]
    if not check_num_position(board, R, C):
        result[t] = 'invalid'
        continue
    if not check_polynomio(board, descrs, R, C):
        result[t] = 'invalid'
        continue
    result[t] = 'valid'
    
print('\n'.join(result))