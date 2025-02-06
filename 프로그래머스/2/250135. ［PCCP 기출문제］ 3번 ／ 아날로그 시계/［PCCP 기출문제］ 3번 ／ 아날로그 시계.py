def solution(h1, m1, s1, h2, m2, s2):
    def get_ring_cnt(h,m,s):
        if h == m == s == 0:
            return 0
        if h >= 12:
            return get_ring_cnt(11, 59, 59) + get_ring_cnt(h-12, m, s)
    
        result = h * 2 * 59 + h + 2 * m - 1
        if 5 * (h + m/60 + s/3600) < s:
            result += 1
        if m + s / 60 < s:
            result += 1
        return result
    
    answer = get_ring_cnt(h2,m2,s2) - get_ring_cnt(h1,m1,s1)
    if (5 * (h2 + m2/60 + s2/3600) == s2
        or
        m2 + s2/60 == s2):
        answer += 1
    return answer