import sys

inputs = [int(sys.stdin.readline()) for _ in range(10)]

cases = [sum(inputs[:i]) for i in range(11)]
min_dif = sys.maxsize
result = 0

for i in range(len(cases)):
    if abs(cases[i] - 100) > min_dif:
        break
    result = max(cases[i], result)
    min_dif = abs(cases[i] - 100)
   
print(result)