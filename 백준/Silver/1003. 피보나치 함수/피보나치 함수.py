import sys
input = sys.stdin.readline

def check(n:int):
    if n <= 1:
        return
    memo[n-1] = memo[n] + memo[n+1]
    check(n-1)

T = int(input())
for _ in range(T):
    n = int(input())
    memo = [0] * (n + 3)
    memo[n] = 1
    memo[n-1] = 1
    check(n-1)
    print(memo[2], memo[1])