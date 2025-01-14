import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(N)]
dishes += dishes[:k-1]

result = 0
choose_dict = defaultdict(int)
for i in range(k):
    choose_dict[dishes[i]] += 1
result = len(choose_dict) if c in choose_dict else len(choose_dict) + 1

for i in range(k, N+k-1):
    choose_dict[dishes[i-k]] -= 1
    if choose_dict[dishes[i-k]] == 0:
        del choose_dict[dishes[i-k]]

    choose_dict[dishes[i]] += 1
    result = max(result, len(choose_dict) if c in choose_dict else len(choose_dict) + 1)
    
print(result)