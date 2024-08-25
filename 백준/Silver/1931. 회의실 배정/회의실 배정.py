import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
cnt = 1
arr.sort(key=lambda tup: (tup[1], tup[0]))
before = arr[0]
for i in range(1, N):
    if before[1] <= arr[i][0]:
        cnt+=1
        before = arr[i]

print(cnt)