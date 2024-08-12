N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
nums2 = list(map(int, input().split()))

results = []

for num in nums2:
    result = 0

    left = 0
    right = N
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] < num:
            left = mid + 1
        elif nums[mid] > num:
            right = mid
        else:
            result = 1
            break

    results.append(result)

print(*results, sep='\n')