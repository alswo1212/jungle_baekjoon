N = int(input())

col_used = [False] * N
diagonal_r = [False] * (N * 2 - 1)
diagonal_l = [False] * (N * 2 - 1)
result = 0

def get_cnt(row_num:int):
    if row_num == N : 
        global result
        result += 1
        return
    
    for i in range(N):
        if (col_used[i] 
            or diagonal_r[i + row_num]
            or diagonal_l[i - row_num + N - 1]) : continue
        

        col_used[i] = diagonal_r[i + row_num] = diagonal_l[i - row_num + N - 1] = True
        get_cnt(row_num + 1)
        col_used[i] = diagonal_r[i + row_num] = diagonal_l[i - row_num + N - 1] = False

get_cnt(0)

print(result)