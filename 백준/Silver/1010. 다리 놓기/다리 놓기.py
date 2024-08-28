n = int(input())
def calc(n, cnt):
    if cnt == 0:
        return 1
    return n * calc(n-1, cnt-1)
for _ in range(n):
    a, b = map(int, input().split())
    big, small = max(a,b), min(a,b)
    memo = [1] * (big + 1)
    for i in range(2, big+1):
        memo[i] = memo[i-1] * i
    print(memo[big] // (memo[big-small] * memo[small]))