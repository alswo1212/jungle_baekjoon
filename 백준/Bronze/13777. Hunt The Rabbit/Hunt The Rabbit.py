import sys
input = sys.stdin.readline
results = []

def bisect(target:int):
    global results
    left, right = 1, 50
    result = []
    while left <= right:
        mid = (left + right) >> 1
        result.append(mid)
        if mid < target:
            left = mid+1
        elif mid > target:
            right = mid - 1
        else:
            break
    results.append(result)

while True:
    num = int(input())
    if num == 0: break
    bisect(num)

for r in results: print(*r)