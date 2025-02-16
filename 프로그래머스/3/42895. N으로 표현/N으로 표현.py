def solution(N, number):
    cases = [set() for _ in range(9)]
    memo = [float('inf')] * (number+1)
    def make_cases(cnt):
        temp = 0
        for i in range(cnt):
            temp *= 10
            temp += N
        cases[cnt].add(temp)

        for i in range(1, cnt):
            for a in cases[i]:
                for b in cases[cnt-i]:
                    cases[cnt].add(a+b)
                    cases[cnt].add(a-b)
                    cases[cnt].add(a*b)
                    if b != 0:
                        temp = a/b
                        if temp // 1 == temp:
                            cases[cnt].add(int(temp))

    for i in range(1, 9):
        make_cases(i)
    
    for i in range(9):
        for num in cases[i]:
            if 0 <= num <= number and memo[num] > i:
                memo[num] = i
    
    return -1 if memo[number] == float('inf') else memo[number]