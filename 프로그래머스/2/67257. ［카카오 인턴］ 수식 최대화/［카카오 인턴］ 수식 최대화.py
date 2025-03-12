from itertools import permutations
def solution(expression:str):
    def calc(num1:int, num2:int, oper:str)->int:
        if oper == '*':
            return num1 * num2
        elif oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
    
    answer = 0
    inputs, opers = [], []
    left = 0
    for i in range(1,len(expression)):
        if not expression[i].isdigit():
            inputs.append(int(expression[left:i]))
            opers.append(expression[i])
            left = i+1
    inputs.append(int(expression[left:]))
    
    use_oper = set(opers)
    for purmut in permutations(use_oper, len(use_oper)):
        c_input = [*inputs]
        c_opers = [*opers]
        for oper in purmut:
            i = 0
            while i < len(c_input)-1:
                if c_opers[i] == oper:
                    c_opers[i:i+1] = []
                    c_input[i:i+2] = [calc(c_input[i],c_input[i+1],oper)]
                    continue
                i+=1
        if abs(c_input[0]) > answer:
            answer = abs(c_input[0])
        
    return answer