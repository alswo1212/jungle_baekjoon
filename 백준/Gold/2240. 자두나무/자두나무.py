import sys
from functools import cache
input = sys.stdin.readline

T, W = map(int, input().split())
positions = [int(input()) for _ in range(T)]

@cache
def solv(idx:int, before:int, rest:int) -> int:
    if idx == len(positions):
        return 0
    
    result = 0
    if before == positions[idx]:
        result = 1 + solv(idx+1, before, rest)
    elif rest == 0:
        result = positions[idx:].count(before)
    else:
        result = max(
            1 + solv(idx+1, positions[idx], rest-1),
            solv(idx+1, before, rest)
        )

    return result

print(solv(0, 1, W))