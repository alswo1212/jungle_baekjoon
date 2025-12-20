import sys
input = sys.stdin.readline
def do_command(command:str, stack:list) -> str:
    commands = command.split()
    if len(commands) == 2:
        stack.append(commands[1])
        return ''
    if commands[0] == '2':
        return '-1' if not stack else stack.pop()
    elif commands[0] == '3':
        return len(stack)
    elif commands[0] == '4':
        return '1' if not stack else '0'
    elif commands[0] == '5':
        return '-1' if not stack else stack[-1]

stack = []
result = []
for _ in range(int(input())):
    temp = do_command(input(), stack)
    if temp != '':
        result.append(temp)

print(*result,sep='\n')