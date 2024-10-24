import sys
input = sys.stdin.readline

l_str = [*input().strip()]
l = int(input())
cur = len(l_str) + 1
r_str = []

for _ in range(l):
    command = input().strip()
    if command == 'L':
        if l_str:
            r_str.append(l_str.pop())
    elif command == 'D':
        if r_str:
            l_str.append(r_str.pop())
    elif command == 'B':
        if l_str:
            l_str.pop()
    else :
        _, x = command.split()
        l_str.append(x)

while r_str:
    l_str.append(r_str.pop())

print(''.join(l_str))