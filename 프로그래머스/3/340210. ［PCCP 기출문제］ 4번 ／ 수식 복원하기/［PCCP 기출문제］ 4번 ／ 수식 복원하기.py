from collections import defaultdict
def solution(expressions):
    def convert(num:int, n:int) -> str:
        if num == 0:
            return '0'
        result = ''
        while num > 0:
            num, mod = divmod(num, n)
            result += str(mod)
        return result[::-1]
    
    def calc(q:str) -> str:
        A, op, B, eq, x = q.split(' ')
        a = int(A, bases[0])
        b = int(B, bases[0])
        temp = a - b if op == '-' else a + b
        std = convert(temp, bases[0])
        if len(bases) == 1:
            return f'{A} {op} {B} {eq} {std}'
        
        for i in range(len(bases)):
            base = bases[i]
            a = int(A, base)
            b = int(B, base)
            temp = a - b if op == '-' else a + b
            convert_num = convert(temp, base)
            if convert_num != std:
                return f'{A} {op} {B} {eq} ?'
            
        return f'{A} {op} {B} {eq} {std}'
    
    hints = []
    querys = []
    min_bases = 2
    for exp in expressions:
        if exp[-1] == 'X':
            querys.append(exp)
        else:
            hints.append(exp)
        for c in exp:
            if c.isdigit():
                n = int(c)
                if min_bases <= n:
                    min_bases = n + 1
    
    base_2_cnt = defaultdict(int)
    for hint in hints:
        A, op, B, eq, C = hint.split(' ')
        for base in range(min_bases, 10):
            a = int(A, base)
            b = int(B, base)
            num = a - b if op == '-' else a + b
            if num == int(C, base):
                base_2_cnt[base] += 1
    bases = list(filter(lambda k: base_2_cnt[k] == len(hints), base_2_cnt.keys()))
    if not bases:
        bases = list(range(min_bases, 10))
    return list(map(calc, querys))