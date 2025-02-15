
def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0])
    visit = set()
    direc = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(n):
        for j in range(m):
            for di in range(4):
                vector = (i,j,di)
                cnt = 0
                while vector not in visit:
                    visit.add(vector)
                    ny, nx = vector[0] + direc[vector[2]][0], vector[1] + direc[vector[2]][1]
                    c = grid[(n+ny)%n][(m+nx)%m]
                    if c == 'L':
                        vector = ((n+ny)%n, (m+nx)%m, (vector[2]-1)%4)
                    elif c == 'R':
                        vector = ((n+ny)%n, (m+nx)%m, (vector[2]+1)%4)
                    else:
                        vector = ((n+ny)%n, (m+nx)%m, vector[2])
                    cnt+=1

                if cnt:
                    answer.append(cnt)
    answer.sort()
    return answer