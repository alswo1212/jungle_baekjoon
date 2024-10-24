string = [*input().strip()]
boom = input().strip()
result = []

string.reverse()
l = len(boom)
while string:
    result.append(string.pop())

    if len(result) < l:
        continue

    flag = True
    for i in range(l):
        if result[-l + i] != boom[i]:
            flag = False
            break

    if flag:
        for _ in range(l) : result.pop()
    
string = ''.join(result)
print("FRULA" if string == '' else string)