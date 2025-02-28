from math import ceil, floor, sqrt
def solution(r1, r2):
    answer = 0
    pow_r1, pow_r2 =  r1*r1, r2*r2
    
    for i in range(1, r2+1):
        r2x = floor(sqrt(pow_r2 - i**2))
        if i >= r1:
            r1x = 0
        else:
            r1x = ceil(sqrt(pow_r1 - i**2))
        answer += r2x-r1x+1
        
    return answer * 4