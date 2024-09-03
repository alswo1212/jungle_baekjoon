import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort(key=lambda n : -n)
max_cal = C // A

cur_cal = C
for i in range(N):
    cur_cal += arr[i]
    cost = A + B * (i+1)
    calc_cal = cur_cal // cost
    if max_cal <= calc_cal:
        max_cal = calc_cal
    else:
        break

print(max_cal)