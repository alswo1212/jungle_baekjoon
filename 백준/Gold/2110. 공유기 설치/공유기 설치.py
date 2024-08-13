import sys

N, C = map(int, input().split())

houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

left = 1
right = houses[-1] - houses[0]
min_distance = 0
while left <= right:
    distance = (left + right) >> 1
    cnt = 1
    current = houses[0]

    for i in range(1, N):
        if houses[i] >= current + distance:
            cnt += 1
            current = houses[i]
    
    if cnt >= C:
        left = distance + 1
        min_distance = distance
    else :
        right = distance - 1


print(min_distance)