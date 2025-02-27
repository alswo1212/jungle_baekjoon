from collections import defaultdict, deque
def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    answer = n*m
    direct = [[1,0],[0,1],[-1,0],[0,-1]]
    containers = defaultdict(set)
    outlines = set()
    # 0: exist 1: in 2: out
    states = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            p = (i,j)
            containers[storage[i][j]].add(p)
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                outlines.add(p)
    def add_out(point:tuple)->list:
        q = deque([point])
        visit = set([point])
        is_out = False
        while q:
            y, x = q.popleft()
            for dy, dx in direct:
                ny, nx = y+dy, x+dx
                if not (0<=ny<n and 0<=nx<m) or states[ny][nx] == 2:
                    is_out = True
                    continue
                np = (ny, nx)
                if np in visit:
                    continue
                if states[ny][nx] == 1:
                    visit.add(np)
                    q.append(np)
        if is_out:
            for y, x in visit:
                states[y][x] = 2
            return list(visit)
        return []
    
    def remove_container(target:list):
        while target:
            p = target.pop()
            added_out = add_out(p)
            while added_out:
                y, x = added_out.pop()
                for dy, dx in direct:
                    ny, nx = y+dy, x+dx
                    if not (0<=ny<n and 0<=nx<m):
                        continue
                    if states[ny][nx] == 0:
                        outlines.add((ny,nx))

    for r in requests:
        if len(r) == 1:
            target = list(filter(lambda p: storage[p[0]][p[1]] == r, outlines))
            answer -= len(target)
            for p in target:
                states[p[0]][p[1]] = 1
                outlines.remove(p)
                containers[r].remove(p)
            remove_container(target)
        else:
            target = list(containers[r[0]])
            answer -= len(target)
            for p in target:
                states[p[0]][p[1]] = 1
                if p in outlines:
                    outlines.remove(p)
                containers[r[0]].remove(p)
            remove_container(target)
    
    return answer