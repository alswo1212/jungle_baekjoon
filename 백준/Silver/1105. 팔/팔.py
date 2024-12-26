L, R = input().strip().split()
lenL, lenR = len(L), len(R)
if lenL != lenR:
    print(0)
else:
    temp = 0
    for i in range(0, lenL):
        if L[i] == R[i] and L[i] == '8':
            temp += 1
        elif L[i] != R[i]:
            break

    print(temp)