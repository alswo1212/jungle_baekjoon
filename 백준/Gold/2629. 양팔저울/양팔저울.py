result = []
n = int(input())
weights = list(map(int, input().split()))
t_cnt = int(input())
targets = list(map(int, input().split()))

dp = [['N'] * 15001 for _ in range(n+1)]
def check_dp(use_cnt, w, weights, dp, max_use):
    if dp[use_cnt][w] == 'Y': return
    dp[use_cnt][w] = 'Y'
    if use_cnt == max_use: return

    check_dp(use_cnt + 1, w + weights[use_cnt], weights, dp, max_use)
    check_dp(use_cnt + 1, w, weights, dp, max_use)
    check_dp(use_cnt + 1, abs(w - weights[use_cnt]), weights, dp, max_use)

check_dp(0, 0, weights, dp, n)

for t in targets: 
    if t > 15000:
        result.append('N')
    else:
        result.append(dp[n][t])
print(*result)