n = int(input())
def solve(n:int):
    temp1 = 1
    temp2 = 2
    if n == 1:
        return temp1
    if n == 2:
        return temp2
    result = temp1 + temp2
    cnt = 3
    while cnt != n:
        temp1, temp2 = temp2, result
        result = (temp1 + temp2) % 10007
        cnt += 1
    return result

print(solve(n))