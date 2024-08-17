import sys
N, M = map(int, sys.stdin.readline().split())

find_arr = [i for i in range(N+1)]
def union_find(arr, num):
    return num if arr[num] == num else union_find(arr, arr[num])

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    u_num = union_find(find_arr, u)
    v_num = union_find(find_arr, v)
    if u_num < v_num:
        find_arr[v_num] = u_num
    else :
        find_arr[u_num] = v_num

for i in range(1, N + 1):
    if find_arr[i] != i:
        find_arr[i] = union_find(find_arr, i)

print(len(set(find_arr)) - 1)