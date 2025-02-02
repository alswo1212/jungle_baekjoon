left, right = map(int, input().split())

nums = set()
for num in range(left, right+1):
    nums.add(num)

i = 2
while i ** 2 <= right:
    temp = i ** 2
    for k in range(temp * (left // temp), right+1, temp):
        if k in nums:
            nums.remove(k)
    i += 1
print(len(nums))