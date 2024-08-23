import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = []

for _ in range(k):
    coin, cnt = map(int, input().split())
    coins.append((coin, cnt))

dp = [0] * (T+1)
dp[0] = 1

for coin, cnt in coins:
    for money in range(T, 0, -1):
        for i in range(1, cnt + 1):
            if money - coin * i >= 0:
                dp[money] += dp[money - coin * i]

print(dp[T])