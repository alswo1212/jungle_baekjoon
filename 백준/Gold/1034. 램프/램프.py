import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
cnts = defaultdict(int)
need_bits = defaultdict(list)
for _ in range(N):
    num = int(input(), 2) 
    cnts[num] += 1
    need_bit = M - bin(num).count('1')
    need_bits[need_bit].append(num)
K = int(input())

result = 0
for bit_cnt in range(K % 2, min(K, M) + 1, 2):
    for num in need_bits[bit_cnt]:
        result = max(result, cnts[num])

print(result)