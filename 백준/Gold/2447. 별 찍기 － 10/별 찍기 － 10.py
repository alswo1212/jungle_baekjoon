N = int(input()) # N = 3^k, k < 8

def isStart(i:int, j:int) -> bool:
    if i == 0 and j == 0:
        return True
    if i % 3 == 1 and j % 3 == 1:
        return False
    
    return isStart(i // 3, j // 3)

temp = []
for i in range(N):
    for j in range(N):
        temp.append('*' if isStart(i, j) else ' ')
    print(''.join(temp))
    temp.clear()