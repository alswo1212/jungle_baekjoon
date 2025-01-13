import sys
from collections import deque
input = sys.stdin.readline

def can_go(points:list) -> bool:
    q = deque([points[0]])
    visit = [False] * len(points)
    visit[0] = True
    while q:
        now = q.popleft()
        if now == points[-1]:
            return True
        for i in range(len(points)):
            if visit[i]:
                continue
            if abs(now[0] - points[i][0]) + abs(now[1] - points[i][1]) > 1000:
                continue
            visit[i] = True
            q.append(points[i])
    return False

T = int(input())
result = []
for _ in range(T):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n+2)]
    result.append('happy' if can_go(points) else 'sad')

print('\n'.join(result))
