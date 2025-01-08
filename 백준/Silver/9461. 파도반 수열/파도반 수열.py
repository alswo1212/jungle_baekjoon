import sys
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]
P = [1] * 101
P[4] = P[5] = 2
for i in range(6, 101): P[i] = P[i-1] + P[i-5]

print('\n'.join(map(lambda num: str(P[num]), nums)))