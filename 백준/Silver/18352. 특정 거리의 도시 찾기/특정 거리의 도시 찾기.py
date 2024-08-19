import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
city_link = [[]for _ in range(N+1)]
for _ in range(M):
    start, to = map(int, sys.stdin.readline().split())
    city_link[start].append(to)

def BFS(city:list, start, K, city_link):
    q = deque([start])
    visit = [False] * len(city)
    visit[start] = True
    
    while q:
        now_city = q.popleft()
        for next_city in city_link[now_city]:
            if visit[next_city] : continue
            city[next_city] = city[now_city] + 1
            visit[next_city] = True
            if city[next_city] == K : continue
            q.append(next_city)
    
    result = [i for i in range(len(city)) if city[i] == K]
    return result

result = BFS([0]*(N+1), X, K, city_link)
if result:
    print(*result, sep='\n')
else:
    print(-1)