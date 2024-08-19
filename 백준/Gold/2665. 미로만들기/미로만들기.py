import sys
from queue import Queue
input = sys.stdin.readline

N = int(input())
board = [input().strip() for _ in range(N)]
visit = [[False] * N for _ in range(N)]

q = Queue()
q.put((0,0))
visit[0][0] = True

direc = [(1,0),(-1,0),(0,-1),(0,1)]
def BFS(q, visit, direc, depth):
    temp = []
    while not q.empty():
        row, col = q.get()
        for i in range(4):
            y,x = direc[i]
            ny = row + y
            nx = col + x
            if (ny < 0 or ny >= N
                or nx < 0 or nx >= N): continue
            if visit[ny][nx] : continue
            if board[ny][nx] == '0':
                visit[ny][nx] = True
                temp.append((ny,nx))
                continue
            if nx == ny == (len(visit) - 1) : 
                return depth
            visit[ny][nx] = True
            q.put((ny,nx))
            
    for item in temp:
        q.put(item)
    return BFS(q, visit, direc, depth + 1)

print(BFS(q, visit, direc, 0))