import sys
n = int(sys.stdin.readline())

arr = [0] * 10_001

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(10_001):
    if arr[i]:
        for _ in range(arr[i]) : print(i)