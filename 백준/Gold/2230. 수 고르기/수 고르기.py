import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
left = right = 0
result = float('inf')
while left <= right:
    dif = arr[right] - arr[left]
    
    if dif > M :
        if result > dif:
            result = dif
        left += 1
    else:
        if dif == M:
            result = dif
        if right == N-1:
            left += 1
        else:
            right += 1
        
print(result)