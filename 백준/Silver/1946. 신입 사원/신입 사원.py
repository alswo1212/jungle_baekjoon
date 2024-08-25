import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort()
    result = 1
    top = 0
    for i in range(1, N):
        if arr[i][1] < arr[top][1]:
            top = i
            result += 1
        
    print(result)