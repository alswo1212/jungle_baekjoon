import sys

n = int(sys.stdin.readline())

stack = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 0
height = 0

while len(stack):
    num = stack.pop()
    if num > height:
        cnt += 1
        height = num

print(cnt)