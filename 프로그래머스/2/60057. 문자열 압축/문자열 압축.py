def solution(s):
    answer = len(s)
    for l in range(1, len(s)//2+1):
        temp = ''
        i = 0
        while i < len(s):
            j = i
            cnt = 0
            while j < len(s) and s[i:i+l] == s[j:j+l]:
                cnt += 1
                j += l
            
            if cnt == 1:
                temp += s[i:j]
                i = j
            else:
                temp += f'{cnt}{s[i:i+l]}'
                i += l*cnt
        answer = min(answer, len(temp))
    return answer