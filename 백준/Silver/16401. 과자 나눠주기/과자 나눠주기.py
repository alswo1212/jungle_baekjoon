import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = [*map(int, input().split())]
left, right = 1, max(snacks)
result = 0

def slipt_snack(length:int) -> int:
    result = 0
    for i in range(N):
        result += snacks[i] // length
    return result

while left <= right:
    mid = (left + right) >> 1
    if mid == 0:
        break
    temp = slipt_snack(mid)
    if temp < M:
        right = mid - 1
    else:
        result = max(mid, result)
        left = mid + 1

print(result)
    