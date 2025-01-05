from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M, e = map(int, input().split())
board = [input().split() for _ in range(N)]
y, x = map(int, input().split())

consumers, ends = set(), []
val2idx = {}
for i in range(M):
    sy, sx, ey, ex = map(int, input().split())
    start, end = (sy-1, sx-1), (ey-1, ex-1)
    consumers.add(start)
    ends.append(end)
    val2idx[start] = i

direc = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs_find(start: tuple, targets: set) -> list:
    if start in targets:
        return [start, 0]
    q = [(0, start)]
    visit = set([start])
    points = []
    min_dist = float('inf')
    while q:
        dist, point = heappop(q)
        if point in targets:
            if dist < min_dist:
                min_dist = dist
                points.append(point)
            elif dist == min_dist:
                points.append(point)
        if dist > min_dist:
            break
        
        for dy, dx in direc:
            ny, nx = point[0] + dy, point[1] + dx
            if not (0 <= ny < len(board) and 0 <= nx < len(board[ny])):
                continue
            if board[ny][nx] == '1':
                continue

            n_point = (ny, nx)
            if n_point in visit:
                continue
            visit.add(n_point)
            heappush(q, (dist+1, n_point))
    if points:
        points.sort()
        return [points[0], min_dist]
    return [None, -1]

def solv(now, e) -> int:
    for _ in range(M):
        consum, move = bfs_find(now, consumers)
        e -= move
        if consum == None or e < 0 or move < 0:
            return -1
        consumers.remove(consum)
            
        end_p = ends[val2idx[consum]]
        temp, move = bfs_find(consum, set([end_p]))
        e -= move
        if temp == None or e < 0 or move < 0:
            return -1
        
        e += 2 * move
        now = end_p
    return e
print(solv((y-1, x-1), e))
