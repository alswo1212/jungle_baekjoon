def solution(key, lock):
    answer = False
    n, m = len(key), len(lock)
    
    def rotate(arr:list)->list:
        return [list(ar[::-1]) for ar in zip(*arr)]
    
    def is_match(arr:list, r:int, c:int)->bool:
        nonlocal n, m, lock
        for i in range(m):
            for j in range(m):
                temp = lock[i][j]
                if 0 <= r+i < n and 0 <= c+j < n:
                    temp += arr[r+i][c+j]
                if temp != 1:
                    return False
                
        return True

    now_key = [[*k] for k in key]
    for _ in range(4):
        now_key = rotate(now_key)

        for r in range(n-1, -m, -1):
            for c in range(n-1, -m, -1):
                if is_match(now_key, r, c):
                    return True
                
    return answer