import sys
input = sys.stdin.readline

N = int(input())
building = [int(input()) for _ in range(N)]

stack = []
cnt = 0
for i in range(N-1, -1, -1):
    if not stack :
        stack.append(i)
        continue

    poped = -1
    while stack and building[stack[-1]] < building[i]:
        poped = stack.pop()
    if stack:
        cnt += stack[-1] - i - 1
    else:
        cnt += N - i - 1
        
    stack.append(i)
print(cnt)