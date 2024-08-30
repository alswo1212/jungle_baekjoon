import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnts = {-1 : 0, 0 : 0, 1 : 0}

def partial(sr, sc, n):
    num = arr[sr][sc]
    if n == 1:
        cnts[num] += 1
        return
    
    flag = True
    for i in range(sr, sr+n):
        for j in range(sc, sc+n):
            if arr[i][j] != num:
                flag = False
                new_n = n//3
                partial(sr,sc,new_n)
                partial(sr,sc+new_n,new_n)
                partial(sr,sc+new_n*2,new_n)
                partial(sr+new_n,sc,new_n)
                partial(sr+new_n,sc+new_n,new_n)
                partial(sr+new_n,sc+new_n*2,new_n)
                partial(sr+new_n*2,sc,new_n)
                partial(sr+new_n*2,sc+new_n,new_n)
                partial(sr+new_n*2,sc+new_n*2,new_n)
                break
        if not flag : break

    if flag:
        cnts[num] += 1

partial(0,0,N)

for num, cnt in cnts.items():
    print(cnt)