import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
load = []
water_q = deque()
hedgehog_q = deque()
visit = [[0] * C for _ in range(R)]

# 입력 처리 및 초기 상태 큐에 추가
for i in range(R):
    row = input().strip()
    load.append(row)
    for j in range(C):
        if row[j] == 'S':
            hedgehog_q.append((i, j))
            visit[i][j] = 1  # 고슴도치 방문
        elif row[j] == '*':
            water_q.append((i, j))
            visit[i][j] = 2  # 물 방문

# 방향 배열 (상하좌우)
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# BFS 수행
def BFS():
    while water_q or hedgehog_q:
        # 먼저 물을 확산시킴
        water_len = len(water_q)
        for _ in range(water_len):
            y, x = water_q.popleft()
            for dy, dx in direc:
                ny, nx = y + dy, x + dx
                if 0 <= ny < R and 0 <= nx < C and load[ny][nx] != 'X' and load[ny][nx] != 'D' and visit[ny][nx] == 0:
                    visit[ny][nx] = 2
                    water_q.append((ny, nx))

        # 그 다음에 고슴도치를 이동시킴
        hedgehog_len = len(hedgehog_q)
        for _ in range(hedgehog_len):
            y, x = hedgehog_q.popleft()
            for dy, dx in direc:
                ny, nx = y + dy, x + dx
                if 0 <= ny < R and 0 <= nx < C:
                    if load[ny][nx] == 'D':
                        return visit[y][x]  # 목적지 도착
                    if load[ny][nx] == '.' and visit[ny][nx] == 0:
                        visit[ny][nx] = visit[y][x] + 1
                        hedgehog_q.append((ny, nx))

    return "KAKTUS"

# 결과 출력
print(BFS())