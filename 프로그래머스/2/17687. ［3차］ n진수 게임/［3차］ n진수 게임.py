def solution(n, t, m, p):
    temp = "0123456789ABCDEF"
    result = []
    num = 0
    while len(result) < t*(m):
        stack = []
        now_num = num
        while now_num >= n:
            stack.append(temp[now_num % n])
            now_num //= n
        result.append(temp[now_num])
        result.extend(stack[::-1])
        num += 1
        
    return ''.join(result[p-1:t*m:m])