A, B, C = map(int, input().split())

def partial_mod(a, b, c):
    if b == 1 : return a % c
    
    mult = 1 if b % 2 == 0 else a
    return partial_mod(a, b >> 1, c) ** 2 * mult % c

print(partial_mod(A, B, C))