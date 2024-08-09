import sys

n = int(input())

inputs = set([sys.stdin.readline().replace('\n', '') for _ in range(n)])

result = sorted(inputs, key=lambda ward:(len(ward), ward))

for r in result : print(r)