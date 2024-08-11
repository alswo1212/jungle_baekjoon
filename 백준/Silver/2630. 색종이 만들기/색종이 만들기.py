import sys
n = int(input())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cuted_paper = []

def cut(start_row, start_col, N):
    color = paper[start_row][start_col]
    for i in range(start_row, start_row + N):
        for j in range(start_col, start_col + N):
            if color == paper[i][j] : continue
            next_N = N >> 1
            cut(start_row, start_col, next_N)
            cut(start_row + next_N, start_col, next_N)
            cut(start_row, start_col + next_N, next_N)
            cut(start_row + next_N, start_col + next_N, next_N)
            return
    
    cuted_paper.append(color)

cut(0, 0, n)
blue_cnt = sum(cuted_paper)
white_cnt = len(cuted_paper) - blue_cnt
print(white_cnt, blue_cnt, sep='\n')
