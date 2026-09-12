from math import sqrt

def is_prime(num:int):
    if num < 2 : return False
    if num <= 3 : return True
    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True

def to_int(s:str): return int(s) if s.isnumeric() else 0

def solution(n, k):
    char_stack = []
    k_nums = ''
    while n:
        char_stack.append(str(n%k))
        n //= k
    while char_stack:
        k_nums += char_stack.pop()
    
    return len(list(filter(is_prime,map(to_int, k_nums.split('0')))))