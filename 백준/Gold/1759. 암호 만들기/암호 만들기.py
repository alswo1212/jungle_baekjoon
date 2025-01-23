from itertools import combinations
import sys
L, C = map(int, input().split())
chars = list(input().split())
chars.sort()
ja_cnt, mo_cnt = 0, 0
mos = set(['a', 'e', 'i', 'o', 'u'])
for combi in combinations(chars, L):
    ja_cnt = mo_cnt = 0
    for c in combi:
        if c in mos:
            mo_cnt += 1
        else:
            ja_cnt += 1
    
    if ja_cnt >= 2 and mo_cnt >= 1:
        sys.stdout.write(f'{''.join(combi)}\n')