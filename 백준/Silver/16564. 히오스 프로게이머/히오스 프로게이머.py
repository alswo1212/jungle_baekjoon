import sys

N, K = map(int, input().split())
heros = [int(sys.stdin.readline()) for _ in range(N)]
heros.sort()

def calc_leveling(level: int) -> int:
    cnt = 0
    for lev in heros :
        if lev >= level: break
        cnt += level - lev
    return cnt

left = 1
right  = heros[-1] + (K // N)
result = heros[-1]

while left <= right:
    target_level = (left + right) >> 1
    need_leveling = calc_leveling(target_level)
    
    if need_leveling < K:
        left = target_level + 1
        result = target_level
    elif need_leveling > K:
        right = target_level - 1
    else : 
        result = target_level
        break

print(result)