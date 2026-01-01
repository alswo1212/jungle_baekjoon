from collections import deque
N = int(input())
max_N = 1
area = []
for _ in range(N):
    heights = []
    for num in map(int, input().split()):
        heights.append(num)
        max_N = max(max_N, num)
    area.append(heights)

def make_safe_area(area:list[list[int]], n:int) -> list[list[bool]]:
    result = []
    for i in range(len(area)):
        row = []
        for num in area[i]:
            row.append(num > n)
        result.append(row)
    return result

def bfs(y:int, x:int, safe_area:list[list[bool]]):
    drec = [[0,1], [0,-1], [1,0], [-1,0]]
    q = deque([[y, x]])
    while q:
        cur_y, cur_x = q.popleft()
        for dy, dx in drec:
            ny, nx = cur_y+dy, cur_x+dx
            if not(0 <= ny < len(safe_area) and 0 <= nx < len(safe_area[ny])): continue
            if not safe_area[ny][nx]: continue
            q.append([ny, nx])
            safe_area[ny][nx] = False

result = 0
for n in range(0, max_N+1):
    safe_area = make_safe_area(area, n)
    sub_result = 0

    for i in range(len(safe_area)):
        for j in range(len(safe_area[i])):
            if safe_area[i][j]:
                sub_result += 1
                bfs(i, j, safe_area)
    
    result = max(result, sub_result)

print(result)