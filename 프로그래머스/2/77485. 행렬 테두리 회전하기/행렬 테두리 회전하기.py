def solution(rows, columns, queries):
    direc = [(0,1),(1,0),(0,-1),(-1,0)]
    def rotate(x1:int,y1:int,x2:int,y2:int)->int:
        result = float('inf')
        temp = board[y1][x1]
        ny, nx = y1, x1
        for dy, dx in direc:
            ny, nx = ny+dy, nx+dx
            while y1<=ny<= y2 and x1<=nx<=x2:
                if result > temp:
                    result = temp
                board[ny][nx], temp = temp, board[ny][nx]
                ny, nx = ny+dy, nx+dx
            ny, nx = ny-dy, nx-dx
        return result

    answer = []
    board = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]
    for r1, c1, r2, c2 in queries:
        answer.append(rotate(c1-1,r1-1,c2-1,r2-1))

    return answer