from collections import defaultdict
def solution(p):
    if p == '':
        return p
    counter = defaultdict(int)
    i = 0
    while i < len(p):
        counter[p[i]] += 1
        i+=1
        if counter['('] == counter[')']:
            break
    
    u, v = p[:i], p[i:]
    if u[0] == '(':
        return u+solution(v)
    
    answer = '(' + solution(v) + ')'
    for i in range(1, len(u)-1):
        if u[i] == ')':
            answer += '('
        else:
            answer += ')'
    return answer