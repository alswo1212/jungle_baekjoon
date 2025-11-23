from collections import deque
N = int(input())
q = deque([i for i in range(1, N+1)])
results = []
while q:
    results.append(q.popleft())
    if not q:
        break
    q.append(q.popleft())

print(*results)