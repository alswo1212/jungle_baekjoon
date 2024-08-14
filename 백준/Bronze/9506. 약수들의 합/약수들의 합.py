import sys
while True:
    num = int(sys.stdin.readline())
    if num == -1 : break
    parts = [1]
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            parts.append(i)
    
    if sum(parts) == num:
        print(f'{num} = {" + ".join(map(str,parts))}')
    else:
        print(f'{num} is NOT perfect.')