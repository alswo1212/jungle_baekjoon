import sys
import heapq
input = sys.stdin.readline

R, C = map(int, input().split())
load = []
q = []
visit = []
for i in range(R):
    row = input()
    load.append(row)
    visit.append([0] * len(row))
    for j in range(len(row)):
        if row[j] == 'S':
            heapq.heappush(q, (1, i, j))
            visit[i][j] = 1
        elif row[j] == '*':
            heapq.heappush(q, (0, i, j))
            visit[i][j] = 2

def BFS(q, load, visit):
    days = 0
    direc = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        days += 1
        for _ in range(len(q)):
            t, y, x = heapq.heappop(q)
            typ = t % 2
            for d in direc:
                ny = y + d[0]
                nx = x + d[1]
                if not(0 <= ny < R) : continue
                if not(0 <= nx < C) : continue
                if load[ny][nx] == 'X': continue

                if typ == 0:
                    if visit[ny][nx] < 2 and load[ny][nx] != 'D':
                        visit[ny][nx] = 2
                        heapq.heappush(q, (t + 2, ny, nx))
                elif typ == 1:
                    if load[ny][nx] == 'D':
                        return days
                    if visit[ny][nx] == 0:
                        visit[ny][nx] = 1
                        heapq.heappush(q, (t + 2, ny, nx))
                
    return 'KAKTUS'

print(BFS(q, load, visit))