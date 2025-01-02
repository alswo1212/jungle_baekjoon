import sys
from functools import cache
from itertools import combinations
input = sys.stdin.readline

@cache
def get_dist(point:tuple, h:tuple) -> int:
    return abs(point[0] - h[0]) + abs(point[1] - h[1])
    
N, M = map(int, input().split())
chickens, houses = [], []
for i in range(N):
    row = input().split()
    for j in range(N):
        if row[j] == '2':
            chickens.append((i,j))
        elif row[j] == '1':
            houses.append((i,j))

result = float('inf')

for c in combinations(chickens, M):
    temp = {}
    for point in c:
        for h in houses:
            temp_dist = get_dist(point, h)
            if h not in temp or temp_dist < temp[h]:
                temp[h] = temp_dist

    temp_result = sum(temp.values())
    if temp_result < result:
        result = temp_result
    
print(result)