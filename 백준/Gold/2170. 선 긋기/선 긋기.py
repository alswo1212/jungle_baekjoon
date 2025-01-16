import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
stack = [lines[0]]
for i in range(1, N):
    line = lines[i]
    if stack[-1][0] <= line[0] <= stack[-1][1]:
        stack[-1][1] = max(stack[-1][1], line[1])
    else:
        stack.append(line)

result = 0
while stack:
    x, y = stack.pop()
    result += y - x
print(result)