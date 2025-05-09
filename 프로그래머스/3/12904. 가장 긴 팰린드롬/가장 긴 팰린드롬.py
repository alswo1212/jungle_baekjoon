def solution(s):
    if s == s[::-1] :
        return len(s)
    for i in range(1, len(s)) :
        n = len(s) - i
        indexList = [x for x in range(len(s) - n + 1)]
        for e in indexList :
            p = s[e: e + n]
            if p == p[::-1] :
                return len(p)
    return -1