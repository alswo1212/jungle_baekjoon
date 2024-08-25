from collections import deque
sic = input().strip()
nums = deque()
temp = []
for s in sic:
    if s == '-' or s == '+':
        nums.append(int(''.join(temp)))
        temp.clear()
        nums.append(s)
        continue
    temp.append(s)
nums.append(int(''.join(temp)))
temp.clear()

result = nums.popleft()
temp = 0
while nums:
    num = nums.pop()
    oper = nums.pop()
    if oper == '+':
        temp += num
    else :
        result -= num
        if temp:
            result -= temp
            temp = 0

if temp:
    result += temp
print(result)