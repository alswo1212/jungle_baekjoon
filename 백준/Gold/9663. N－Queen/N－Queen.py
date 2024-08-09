N = int(input())

col_used = [False] * N
diagonal_r = [False] * (N << 1) # /
diagonal_l = [False] * (N << 1) # \
result = 0

def get_cnt(row_num:int):
    if row_num == N : 
        global result
        result += 1
        return
    
    for i in range(N if row_num else N >> 1):
        if (col_used[i] 
            or diagonal_r[i + row_num]
            or diagonal_l[row_num - i]) : continue
        
        col_used[i] = diagonal_r[i + row_num] = diagonal_l[row_num - i] = True
        get_cnt(row_num + 1)
        col_used[i] = diagonal_r[i + row_num] = diagonal_l[row_num - i] = False

get_cnt(0)
result <<= 1

if N % 2:
    mid = N >> 1
    col_used[mid] = diagonal_l[-mid] = diagonal_r[mid] = True
    get_cnt(1)

print(result)