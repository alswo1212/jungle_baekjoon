import sys
input = sys.stdin.readline

def is_in(point:tuple, circle:tuple) -> bool:
    return (circle[0] - point[0]) ** 2 + (circle[1] - point[1]) ** 2 < circle[2] ** 2

T = int(input())
result = []
for _ in range(T):
    sx, sy, ex, ey = map(int, input().split())
    cnt = 0
    start, end = (sx, sy), (ex, ey)
    for _ in range(int(input())):
        circle = tuple(map(int, input().split())) 

        if is_in(start, circle) ^ is_in(end, circle):
            cnt += 1
    result.append(cnt)

print(*result, sep='\n')