N = int(input())
TPs = [list(map(int, input().split())) for _ in range(N)]

memo = [-1] * N
def earn(idx:int) -> int:
    global N, TPs, memo
    if idx >= N:
        return 0
    
    if memo[idx] != -1:
        return memo[idx]
    
    if idx + TPs[idx][0] > N:
        memo[idx] = earn(idx+1)
    else:
        memo[idx] = max(earn(idx+1), earn(idx + TPs[idx][0]) + TPs[idx][1])
    return memo[idx]

print(earn(0))