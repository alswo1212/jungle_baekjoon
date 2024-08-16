ps = input().strip()
stack = []
flag = True

for s in ps:
    if s == '(' or s == '[':
        stack.append(s)
        continue
    
    pare = '(' if s == ')' else '['
    reduce = 0
    meet_pare = False
    while len(stack) != 0:
        poped = stack.pop()
        if poped == pare : 
            meet_pare = True
            break
        if type(poped) is str:
            flag = False
            break
        reduce += poped
    
    if not flag or not meet_pare:
        print(0)
        flag = False
        break

    if reduce == 0: reduce = 1
    stack.append(reduce * (2 if pare == '(' else 3))

if flag:
    print(0 if type(stack[0]) is str else sum(stack))