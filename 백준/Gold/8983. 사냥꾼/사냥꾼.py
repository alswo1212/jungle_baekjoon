import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())

hunt_point = list(map(int,input().split()))
hunt_point.sort()

result = 0

animals = []
for _ in range(N):
    animal = tuple(map(int, input().split()))
    if animal[1] > L : continue
    animals.append(animal)

def search_hunter(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        
        if hunt_point[mid] == target:
            return hunt_point[mid]
        
        if hunt_point[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    if start >= len(hunt_point):
        return hunt_point[end]
    if end < 0:
        return hunt_point[start]
    
    if abs(hunt_point[start] - target) < abs(hunt_point[end] - target):
        return hunt_point[start]
    else:
        return hunt_point[end]

for animal in animals:
    hp = search_hunter(0, M - 1, animal[0])
    if abs(hp - animal[0]) + animal[1] <= L:
        result += 1

print(result)