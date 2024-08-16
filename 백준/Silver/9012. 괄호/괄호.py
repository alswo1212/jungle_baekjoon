import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    ps = sys.stdin.readline().strip()
    flag = False
    for s in ps:
        if s == '(':
            stack.append(s)
        else :
            if len(stack) == 0:
                sys.stdout.write('NO\n')
                flag = True
                break
            stack.pop()
    
    if not flag:
        sys.stdout.write(f'{"NO" if len(stack) else "YES"}\n')
    stack.clear()