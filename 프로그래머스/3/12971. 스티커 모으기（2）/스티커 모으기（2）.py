import sys
sys.setrecursionlimit(10**6)
def solution(sticker):
    n = len(sticker)
    # 0 : 0 선택, 1: 0 선택 x
    memo = [[-1] * n for _ in range(2)]
    def dp(idx:int, a:int)->int:
        if not (0 <= a < n):
            return 0
        if memo[idx][a] != -1:
            return memo[idx][a]
        
        if idx == 0:
            if a == 0:
                memo[idx][a] = sticker[a] + dp(idx,a+2)
            elif a == n-1:
                memo[idx][a] = 0
            else:
                memo[idx][a] = max(sticker[a] + dp(idx,a+2), dp(idx,a+1))
        else:
            if a == 0:
                memo[idx][a] = dp(idx,a+1)
            else:
                memo[idx][a] = max(sticker[a] + dp(idx,a+2), dp(idx,a+1))
        return memo[idx][a]
    dp(0,0)
    dp(1,0)
    return max(memo[0][0], memo[1][0])