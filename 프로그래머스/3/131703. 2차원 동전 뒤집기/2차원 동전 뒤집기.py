def solution(beginning, target):
    answer = 0
    n, m = len(beginning), len(beginning[0])
    diff = [[0]*m for _ in range(n)]
    def init_diff():
        for i in range(n):
            for j in range(m):
                diff[i][j] = beginning[i][j] ^ target[i][j]
    def swip_row(num):
        result = 0
        for i in range(n):
            if diff[i][0] == num:
                result += 1
                for j in range(m):
                    diff[i][j] ^= 1
        return result
    def swip_col(num):
        result = 0
        for j in range(m):
            if diff[0][j] == num:
                result += 1
                for i in range(n):
                    diff[i][j] ^= 1
        return result
    
    init_diff()
    answer = swip_col(1) + swip_row(1)
    init_diff()
    answer = min(answer, swip_row(1) + swip_col(1))
    init_diff()
    answer = min(answer, swip_row(0) + swip_col(1))
    init_diff()
    answer = min(answer, swip_col(0) + swip_row(1))
    

    for i in range(n):
        for j in range(m):
            if diff[i][j]:
                return -1
    return answer