import sys
input = sys.stdin.readline
foul = 0
inputs = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    if not(y >= x and y >= -x):
        foul += 1
        continue
    
    inputs.append(x*x+y*y)
inputs.sort()

for _ in range(int(input())):
    R = int(input())
    R = R * R
    start = 0
    end = len(inputs) - 1

    while start <= end:
        mid = (start + end) >> 1
        if inputs[mid] > R:
            end = mid - 1
        else:
            start = mid + 1
    
    sys.stdout.write(f'{foul} {start} {len(inputs) - start}\n')