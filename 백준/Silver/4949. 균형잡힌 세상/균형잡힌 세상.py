import sys

def is_balance(line:str) -> str:
    stack = []
    for c in line:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return 'no'
            stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                return 'no'
            stack.pop()
    return 'yes' if len(stack) == 0 else 'no'

print(*map(is_balance, sys.stdin.readlines()[:-1]), sep='\n')
    