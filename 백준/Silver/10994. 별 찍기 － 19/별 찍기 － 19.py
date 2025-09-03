N = int(input())

def makeStart(num:int):
    if num == 1:
        return [['*']]
    temp = makeStart(num-1)
    length = len(temp)
    result = [
        ['*'] * (length + 4),
        ['*'] + [' '] * (length + 2) + ['*'],
    ]
    for t in temp:
        result.append(['*', ' '] + t + [' ', '*'])
    result.append(['*'] + [' '] * (length + 2) + ['*'])
    result.append(['*'] * (length + 4),)

    return result

for arr in makeStart(N):
    print(''.join(arr))