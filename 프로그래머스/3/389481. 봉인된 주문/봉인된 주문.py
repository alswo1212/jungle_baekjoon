def solution(n, bans):
    def str_2_int(ban)->int:
        result = 0
        p = 1
        for c in ban[::-1]:
            result += (ord(c)-96) * p
            p *= 26
        return result
    
    bans.sort(key=lambda s: (len(s), s))
    for ban in bans:
        ban_num = str_2_int(ban)
        if ban_num <= n:
            n += 1
        else:
            break
    
    stack = []
    while n:
        stack.append(chr((n-1)%26 + 97))
        n = (n-1) // 26

    return ''.join(stack[::-1])