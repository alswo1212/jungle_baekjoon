def solution(n, l, r):
    cache = {}
    def one_or_zero(num:int)->int:
        if num in cache:
            return cache[num]
        while num:
            if num % 5 == 2:
                cache[num] = 0
                return 0
            num = num // 5
        cache[num] = 1
        return 1
    
    return sum(one_or_zero(i-1) for i in range(l, r+1))