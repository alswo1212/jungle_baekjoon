import sys

def calc(temp:str):
    temp = temp.replace('{}', '')
    stack = []
    cnt = 0
    for s in temp:
        if not stack:
            if s == '}':
                cnt += 1
                stack.append('{')
            else:
                stack.append(s)
            continue

        if s == '}' and stack[-1] == '{':
            stack.pop()
            continue
        stack.append(s)
    return (len(stack) >> 1) + cnt

number = 0
while True:
    temp = sys.stdin.readline().strip()
    if temp[0] == '-':
        break
    result = calc(temp)
    number += 1
    sys.stdout.write(f'{number}. {result}\n')