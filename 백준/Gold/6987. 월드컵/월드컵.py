from itertools import combinations
def solv(depth:int, arr:list) -> bool:
    if depth == 15:
        return sum(query) == 0
    
    p1, p2 = plays[depth]
    p1 *= 3
    p2 *= 3
    for i, j in cases:
        if arr[p1 + i] > 0 and arr[p2 + j] > 0:
            arr[p1 + i] -= 1
            arr[p2 + j] -= 1
            if solv(depth+1, arr):
                return True
            arr[p1 + i] += 1
            arr[p2 + j] += 1
    
    return False

result = [0] * 4
plays = list(combinations(range(6),2))
cases = [(0, 2), (1, 1), (2, 0)]
for i in range(4):
    query = list(map(int, input().split()))
    if solv(0, query):
        result[i] = 1

print(*result)