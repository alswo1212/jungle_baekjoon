import sys

n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
points.sort()

def calc_distance(start, end):
    min_distance = int(1e10)
    for i in range(start, end - 1):
        for j in range(i+1, end):
            min_distance = min((points[j][0]-points[i][0]) ** 2 + (points[j][1]-points[i][1]) ** 2, min_distance)
    return min_distance

def divide_conquer(left_idx, right_idx):
    if right_idx - left_idx <= 3:
        return calc_distance(left_idx, right_idx)
    
    mid_idx = (left_idx + right_idx) // 2

    left_distance = divide_conquer(left_idx, mid_idx)
    rigth_distance = divide_conquer(mid_idx, right_idx)

    min_distance = min(left_distance, rigth_distance)

    points_for_check = []
    mid_x = points[mid_idx][0]
    for i in range(left_idx, right_idx):
        if (points[i][0] - mid_x) ** 2 < min_distance : 
            points_for_check.append(points[i])
    points_for_check.sort(key=lambda p: p[1])

    length = len(points_for_check)
    for i in range(length):
        cp1 = points_for_check[i]
        for j in range(i + 1, length):
            cp2 = points_for_check[j]
            if (cp2[1] - cp1[1]) ** 2 >= min_distance : break
            min_distance = min((cp2[0] - cp1[0]) ** 2 + (cp2[1] - cp1[1]) ** 2, min_distance)
    
    return min_distance

print(divide_conquer(0, n))