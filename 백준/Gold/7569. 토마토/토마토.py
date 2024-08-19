import sys
from collections import deque
input = sys.stdin.readline

N, M ,H = map(int, input().split())
box_tower = []
q = deque([])
for h in range(H):
    arr = []
    for y in range(M):
        temp = list(map(int, input().split()))
        for x in range(N):
            if temp[x] == 1:
                q.append((y, x, h))
        arr.append(temp)
    box_tower.append(arr)

if q:
    # 앞 뒤 좌 우 상 하
    # y x h
    direc = [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
    temp = []
    cnt = 0
    while q:
        cur_y, cur_x, cur_h = q.popleft()
        for d in direc:
            ny = cur_y + d[0]
            nx = cur_x + d[1]
            nh = cur_h + d[2]
            if not (0 <= ny < M
                and 0 <= nx < N
                and 0 <= nh < H):continue
            if box_tower[nh][ny][nx] != 0 : continue
            temp.append((ny,nx,nh))
            box_tower[nh][ny][nx] = 1
        if not q:
            cnt += 1
            q.extend(temp)
            temp.clear()

    def check_box(box_tower):
        for h in box_tower:
            for y in h:
                for x in y:
                    if x == 0: return False
        return True
    print(cnt - 1 if check_box(box_tower) else -1)
else :
    print(-1)