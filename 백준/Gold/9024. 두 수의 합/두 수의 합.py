import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int,sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    min_val = sys.maxsize
    cnt = 0
    start = 0
    end = n-1
    while start < end:
        dif = nums[start] + nums[end] - k
        if min_val > abs(dif):
            cnt = 1
            min_val = abs(dif)
        elif min_val == abs(dif):
            cnt += 1
        
        if dif <= 0:
            start += 1
        elif dif > 0:
            end -= 1
    
    print(cnt)