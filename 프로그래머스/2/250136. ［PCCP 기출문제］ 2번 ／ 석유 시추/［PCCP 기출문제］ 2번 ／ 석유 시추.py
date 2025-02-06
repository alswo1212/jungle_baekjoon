from collections import deque
def solution(land):
    def bfs(i,j):
        direc = [(1,0),(0,1),(-1,0),(0,-1)]
        result = 0
        q = deque([(i,j)])
        land[i][j] = 0
        min_x, max_x = len(land[0]), 0
        while q:
            y, x = q.popleft()
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            result += 1

            for dy, dx in direc:
                ny, nx = dy+y, dx+x
                if not (0 <= ny < len(land) and 0 <= nx < len(land[ny])):
                    continue
                if land[ny][nx] == 0:
                    continue

                land[ny][nx] = 0
                q.append((ny,nx))

        return (result, min_x, max_x)

    arr = [0] * len(land[0])
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] == 0:
                continue
            cnt, start, end = bfs(i,j)
            for k in range(start, end+1):
                arr[k] += cnt
    
    return max(arr)