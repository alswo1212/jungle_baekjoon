import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda tup: -tup[1])
result = arr[0][1]

for d, t in arr:
    if t < result:
        result = t
    result -= d

print(result)