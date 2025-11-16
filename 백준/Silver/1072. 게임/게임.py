X, Y = map(int, input().split())

calc = lambda x,y : y * 100 // x
target = calc(X, Y) + 1
result = -1
left, right = 0, X
while left <= right:
    mid = ((right - left) >> 1) + left
    temp = calc(X+mid, Y+mid)
    if temp < target:
        left = mid + 1
    else :
        result = mid
        right = mid - 1

print(result)