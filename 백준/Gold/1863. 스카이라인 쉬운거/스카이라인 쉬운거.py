import sys
input = sys.stdin.readline
N = int(input())

height = [0]
result = 0

for _ in range(N):
    x, y = map(int, input().split())
    while height and height[-1] > y:
        height.pop()
    result += 0 if height[-1] == y else 1
    height.append(y)

print(result)