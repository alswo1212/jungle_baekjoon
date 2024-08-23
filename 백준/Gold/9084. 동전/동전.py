import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target+1)
    dp[0] = 1
    for coin in coins:
        for t in range(target, 0, -1):
            for i in range(t // coin + 1, 0, -1):
                if t - coin * i >= 0:
                    dp[t] += dp[t - coin * i]
    
    print(dp[target])