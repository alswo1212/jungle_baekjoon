import sys

result_min = sys.maxsize
result_max = -(10 ** 9)

n = int(input())

nums = list(map(int, input().split()))
oper_cnts = list(map(int, input().split()))
opers = ['+'] * oper_cnts[0] + ['-'] * oper_cnts[1] + ['*'] * oper_cnts[2] + ['/'] * oper_cnts[3] 
visit = [False] * len(opers)

def dfs(depth, calc):
    if depth == n : 
        global result_max, result_min
        result_max = max(result_max, calc)
        result_min = min(result_min, calc)
        return
    
    for i in range(len(opers)):
        if visit[i] : continue

        visit[i] = True
        dfs(depth+1, calculate(calc, nums[depth], opers[i]))
        visit[i] = False

def calculate(num1, num2, oper):
    if oper == '+' : return num1 + num2
    elif oper == '-' : return num1 - num2
    elif oper == '*' : return num1 * num2

    # 나눗셈인데 하나만 음수일때
    if num1 * num2 < 0: return -(abs(num1) // abs(num2))
    return num1 // num2

dfs(1, nums[0])

print(result_max, result_min, sep='\n')