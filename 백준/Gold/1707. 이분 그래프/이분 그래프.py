import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
def is_bipartite(V, E):
    links = [[] for _ in range(V)]
    for _ in range(E):
        a,b = map(int, input().split())
        links[a - 1].append(b - 1)
        links[b - 1].append(a -1)

    q = deque()
    color = [-1] * V
    size = 1
    time = 0
    for i in range(V):
        if color[i] == -1:
            q.append(i)
            while q:
                if size == 0:
                    size = len(q)
                    time += 1
                poped = q.popleft()
                size -= 1
                if color[poped] != -1:
                    if color[poped] != time % 2:
                        return False
                    continue
                color[poped] = time % 2
                q.extend(links[poped])

    return True

for _ in range(n):
    V, E = map(int,input().split())
    
    print('YES' if is_bipartite(V, E) else 'NO')