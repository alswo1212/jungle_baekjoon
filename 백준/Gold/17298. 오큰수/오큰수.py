N = int(input())
inputs = list(map(int, input().split()))
stack = []
for i in range(N-1, -1, -1):
    temp = inputs[i]
    while stack and stack[-1] <= temp:
        stack.pop()
    inputs[i] = stack[-1] if stack else -1
    stack.append(temp)

print(*inputs)