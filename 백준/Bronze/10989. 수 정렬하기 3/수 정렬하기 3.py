import sys
N = int(input())

cnts = [0] * 10_001

for _ in range(N):
    idx = int(sys.stdin.readline())
    cnts[idx] += 1

for i in range(len(cnts)):
    if cnts[i] == 0 : continue
    for _ in range(cnts[i]):
        sys.stdout.write(f'{i}\n')