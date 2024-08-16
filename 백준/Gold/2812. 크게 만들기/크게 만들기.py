n, k = map(int, input().split())
nums = list(map(int, [*input()]))
stack = [nums[0]]
cnt = k
for i in range(1, n):
    while stack and cnt > 0:
        if nums[i] > stack[-1]:
            stack.pop()
            cnt -= 1
            continue
        break
    stack.append(nums[i])
    
if cnt:
    print(*stack[:-cnt], sep='')
else :
    print(*stack, sep='')