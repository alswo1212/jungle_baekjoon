from collections import deque
N, X = map(int, input().split())

result = 0
visit = [False] * 100_001
q = deque([(N,0)])

def check_visit(num:int, visit:list[bool]):
    result = False
    if 0 <= num < 100_001 and not visit[num]:
        visit[num] = True
        result = True
    return result

while q:
    num, cnt = q.popleft()
    if num == X:
        result = cnt
        break
    if check_visit(num+1, visit): q.append((num+1, cnt+1))
    if check_visit(num-1, visit): q.append((num-1, cnt+1))
    if check_visit(num*2, visit): q.append((num*2, cnt+1))
    
print(result)