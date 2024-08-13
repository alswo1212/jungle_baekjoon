n = int(input())

nums = list(map(int, input().split()))
nums.sort()

left = 0
right = n - 1
std = 1e10
result = [nums[left], nums[right]]

while left < right:
    temp = nums[left] + nums[right]
    
    if abs(temp) < std:
        std = abs(temp)
        result[0] = nums[left]
        result[1] = nums[right]
        if std == 0 : break
    
    if temp > 0:
        right -= 1
    elif temp < 0:
        left += 1

print(result[0], result[1])