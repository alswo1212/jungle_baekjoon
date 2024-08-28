n = int(input())
memo = [1] * (31)
for i in range(2, 31):
    memo[i] = memo[i-1] * i
for _ in range(n):
    a, b = map(int, input().split())
    big, small = max(a,b), min(a,b)
    print(memo[big] // (memo[big-small] * memo[small]))