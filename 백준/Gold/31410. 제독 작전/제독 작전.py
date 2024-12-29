import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
l, r, answer = arr[0][1], arr[-1][1], float('inf')

for i in range(1, N):
    if arr[i][0] == arr[-1][0]:
        answer = min(answer, l)
    l += arr[i][1] + i * (arr[i][0] - arr[i-1][0])

for i in range(N-2, -1, -1):
    if i == 0:
        answer = min(answer, r)
    r += arr[i][1] + (N - 1 - i) * (arr[i+1][0] - arr[i][0])

for i in range(0, N):
    answer = min(answer, 
                 l - (arr[i][1] + arr[-1][0] - arr[i][0]), 
                 r - (arr[i][1] + arr[i][0] - arr[0][0]))

print(answer)