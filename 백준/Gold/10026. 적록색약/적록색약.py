from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
picture = [input().strip() for _ in range(N)]

def bfs(board:list[list[int]], startY:int, startX:int) -> int:
    direc = [(1,0),(0,1),(-1,0),(0,-1)]
    q = deque([(startY, startX)])
    target = board[startY][startX]
    board[startY][startX] = -1

    while q:
        y, x = q.popleft()
        for dy, dx in direc:
            ny, nx = y+dy, x+dx
            if not (0 <= ny < len(board) and 0 <= nx < len(board[ny])):
                continue
            if board[ny][nx] != target:
                continue
            
            board[ny][nx] = -1
            q.append((ny, nx))

def count_picture_area(bit_picture:list[list[int]]) -> int:
    cnt = 0
    for i in range(len(bit_picture)):
        for j in range(len(bit_picture[i])):
            if bit_picture[i][j] == -1: continue
            bfs(bit_picture, i, j)
            cnt += 1
    return cnt

def convert_picture(picture:list[str], bundles:list[str]) -> list[list[int]]:
    result = []
    for i in range(len(picture)):
        row = []
        for j in range(len(picture[i])):
            for idx, bundle in enumerate(bundles):
                if picture[i][j] in bundle:
                    row.append(idx)
                    break
        result.append(row)
    return result
            
r_g_blindness = convert_picture(picture, ['RG', 'B'])
nomal = convert_picture(picture, ['R', 'G', 'B'])

print(count_picture_area(nomal), count_picture_area(r_g_blindness))