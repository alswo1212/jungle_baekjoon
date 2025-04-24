def solution(n, s):
    answer = []
    while n != 0:
        temp = s // n
        if temp == 0:
            return [-1]
        answer.append(temp)
        n -= 1
        s -= temp
    
    return answer