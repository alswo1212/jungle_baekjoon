import sys
input = sys.stdin.readline
n = int(input())
def do_prime(n:int):
    if n == 1:
        return
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            do_prime(n // i)
            break

do_prime(n)