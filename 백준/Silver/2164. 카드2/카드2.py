from collections import deque
dq = deque([i + 1 for i in range(int(input()))])

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq[0])