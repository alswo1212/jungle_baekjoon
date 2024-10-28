from itertools import combinations
N, M = map(int, input().split())
result = 0
for combi in combinations(list(map(int, input().split())), 3):
    case = sum(combi)
    if result < case <= M:
        result = case
print(result)