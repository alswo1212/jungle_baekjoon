A, B, C = map(int, input().split())

def custom_pow(a, b, c):
    if b == 1 : return a % c
    else :
        temp = custom_pow(a, b >> 1, c)

        if b % 2 == 0 : return (temp ** 2) % c
        else : return (temp ** 2 * a) % c

print(custom_pow(A, B, C))