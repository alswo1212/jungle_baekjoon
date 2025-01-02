import sys
input = sys.stdin.readline

def make_cases(start:int, cnt:int, temp_list: list):
    if cnt == 0:
        return
    for i in range(start, len(chickens)):
        temp = [*temp_list, chickens[i]]
        cases.append(temp)
        make_cases(i+1, cnt-1, temp)
    
direc = [[1,0],[0,1],[-1,0],[0,-1]]
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
cases = []
make_cases(0, M, [])

for c in cases:
    temp = {}
    for point in c:
        for h in houses:
            temp_dist = abs(point[0] - h[0]) + abs(point[1] - h[1])
            if h not in temp or temp_dist < temp[h]:
                temp[h] = temp_dist

    temp_result = sum(temp.values())
    if temp_result < result:
        result = temp_result
    
print(result)