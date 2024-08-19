import sys
import heapq
input = sys.stdin.readline

R, C = map(int, input().split())
load = []
q = []
visit = []

# 초기 상태 설정
for i in range(R):
    row = input().strip()
    load.append(row)
    visit.append([0] * C)
    for j in range(C):
        if row[j] == 'S':
            heapq.heappush(q, (1, i, j))
            visit[i][j] = 1  # 고슴도치 방문
        elif row[j] == '*':
            heapq.heappush(q, (0, i, j))
            visit[i][j] = 2  # 물 방문

def BFS(q, load, visit):
    direc = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        t, y, x = heapq.heappop(q)
        typ = t % 2  # 물(0)과 고슴도치(1) 구분

        for d in direc:
            ny = y + d[0]
            nx = x + d[1]
            if not (0 <= ny < R and 0 <= nx < C):
                continue
            if load[ny][nx] == 'X':  # 벽이면 지나갈 수 없음
                continue
            
            if typ == 0:  # 물 확산
                if visit[ny][nx] == 0 and load[ny][nx] != 'D':  # 방문하지 않은 곳이면 확산
                    visit[ny][nx] = 2
                    heapq.heappush(q, (t + 2, ny, nx))
            elif typ == 1:  # 고슴도치 이동
                if load[ny][nx] == 'D':  # 목적지 도착
                    return t // 2 + 1  # 이동한 일 수 반환
                if visit[ny][nx] == 0:  # 방문하지 않은 곳
                    visit[ny][nx] = 1
                    heapq.heappush(q, (t + 2, ny, nx))

    return 'KAKTUS'

print(BFS(q, load, visit))