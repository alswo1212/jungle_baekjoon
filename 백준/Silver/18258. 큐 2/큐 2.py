import sys
from collections import deque
def f():
    n = int(sys.stdin.readline())
    dq = deque()
    result = []
    for _ in range(n):
        inputs = sys.stdin.readline().split()
        if inputs[0] == 'push':
            dq.append(inputs[1])
        elif inputs[0] == 'pop':
            result.append(dq.popleft() if dq else -1)
        elif inputs[0] == 'size':
            result.append(len(dq))
        elif inputs[0] == 'empty':
            result.append(0 if dq else 1)
        elif inputs[0] == 'front':
            result.append(dq[0] if dq else -1)
        elif inputs[0] == 'back':
            result.append(dq[-1] if dq else -1)
    return '\n'.join(map(str,result))

print(f())