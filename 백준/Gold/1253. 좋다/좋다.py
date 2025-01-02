N = int(input())
arr = list(map(int, input().split()))
arr.sort()
goods = set()
cnt = 0
for i in range(N):
    if arr[i] in goods:
        cnt += 1
        continue
    
    left, right = 0, N-1
    while left < right:
        temp = arr[left] + arr[right]
        if arr[i] == temp:
            if left == i or right == i:
                if left == i:
                    left += 1
                else:
                    right -= 1
                continue
            cnt += 1
            goods.add(arr[i])
            break
        elif arr[i] < temp:
            right -= 1
        else:
            left += 1
print(cnt)