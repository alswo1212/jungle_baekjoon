import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
for _ in range(k):
    q_length, target_index = map(int, input().split())
    q = deque()
    prioritys = []
    for i, priority in enumerate(map(int, input().split())):
        q.append((i, priority))
        prioritys.append(priority)
    prioritys.sort()

    cnt = 0
    while q:
        polled = q.popleft()
        if polled[1] == prioritys[-1]:
            prioritys.pop()
            cnt += 1
            if polled[0] == target_index:
                print(cnt)
                break
        else:
            q.append(polled)
