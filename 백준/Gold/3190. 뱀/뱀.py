import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    r, c =  map(int, input().split())
    board[r-1][c-1] = 1

L = int(input())
inputs = [input().split() for _ in range(L)]
for arr in inputs:
    arr[0] = int(arr[0])

# 우 하 좌 상
direc = deque([(0,1), (1, 0), (0, -1), (-1, 0)])
str_to_direc = {'L':1, 'D':-1}

second = 1
now_p = [0,0]
game_end = False
snake = deque([(0,0)])
d_idx = 0

while True:
    new_r = now_p[0] + direc[0][0]
    new_c = now_p[1] + direc[0][1]
    if (new_r < 0 
        or new_r >= N
        or new_c < 0
        or new_c >= N):
        game_end = True
        break

    snake.appendleft((new_r, new_c))
    if snake.count((new_r, new_c)) == 2:
        game_end = True
        break

    if board[new_r][new_c] == 1:
        board[new_r][new_c] = 0
    else :
        snake.pop()

    now_p[0] = new_r
    now_p[1] = new_c
    second += 1
    if d_idx < L:
        if second > inputs[d_idx][0]:
            direc.rotate(str_to_direc[inputs[d_idx][1]])
            d_idx += 1

print(second)