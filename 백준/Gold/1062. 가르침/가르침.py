import sys
from itertools import combinations
input = sys.stdin.readline

def word_2_mask(s:str):
    result = 0
    for c in s:
        result |= 1 << (ord(c) - ord('a'))
    return result

N, K = map(int, input().strip().split())
inputs = [word_2_mask(input().strip()) for _ in range(N)]
base_mask = word_2_mask('antic')

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    removable = [1 << i for i in range(26) if (base_mask & (1 << i)) == 0]

    max_cnt = 0
    for chars in combinations(removable, K-5):
        condition_mask = sum(chars) | base_mask
        cnt = 0
        for mask in inputs:
            if mask | condition_mask == condition_mask:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    print(max_cnt)