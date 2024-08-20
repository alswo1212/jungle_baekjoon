import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [[] for _ in range(n)]
cnts = [0] * n
for _ in range(m):
    now, to, time = map(int, input().split())
    edges[now-1].append([to-1, time])
    cnts[to-1] += 1
    
s, t = map(int, input().split())

q = deque([s-1])
times = [0] * n
roads = [[] for _ in range(n)]

while q:
    now = q.popleft()

    for next, pay_time in edges[now]:
        temp_time = pay_time + times[now]
        if temp_time > times[next]:
            times[next] = temp_time
            roads[next] = [now]
        elif temp_time == times[next]:
            roads[next].append(now)
            
        cnts[next] -= 1
        if cnts[next] == 0:
            q.append(next)

q = deque([t-1])
result = set()
while q:
    now = q.popleft()
    for x in roads[now]:
        if (now, x) not in result:
            result.add((now,x))
            q.append(x)

print(times[n-1])
print(len(result))