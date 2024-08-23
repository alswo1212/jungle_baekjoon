import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

lcs = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else :
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

y, x = len(str1), len(str2)
if lcs[y][x]:
    length = lcs[y][x]
    stack = []
    while len(stack) != length:
        if str1[y-1] == str2[x-1]:
            stack.append(str1[y-1])
            y, x= y-1, x-1
        else:
            if lcs[y-1][x] > lcs[y][x-1]:
                y-=1
            else:
                x-=1
    result = ''
    while stack: result += stack.pop()
    print(length)
    print(result)
else:
    print(0)