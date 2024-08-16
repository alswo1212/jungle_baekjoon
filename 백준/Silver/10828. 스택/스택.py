import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    inputs = sys.stdin.readline().split()
    if inputs[0] == 'push':
        stack.append(inputs[1])
    elif inputs[0] == 'pop':
        sys.stdout.write(f'{-1 if len(stack) == 0 else stack.pop()}\n')
    elif inputs[0] == 'size':
        sys.stdout.write(f'{len(stack)}\n')
    elif inputs[0] == 'empty':
        sys.stdout.write(f'{1 if len(stack) == 0 else 0}\n')
    elif inputs[0] == 'top':
        sys.stdout.write(f'{-1 if len(stack) == 0 else stack[-1]}\n')