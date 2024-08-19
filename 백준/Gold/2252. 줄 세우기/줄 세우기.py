import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
student_cnt = [0] * N
q = deque()
arr = [[] for _ in range(N)]

for _ in range(M):
    num1, num2 = map(lambda n: int(n) - 1,input().split())
    student_cnt[num2] += 1
    arr[num1].append(num2)

result = []
for i in range(N):
    if student_cnt[i] == 0:
        q.append(i)

while q:
    s_num = q.popleft()
    result.append(s_num + 1)
    for n in arr[s_num]:
        student_cnt[n] -= 1
        if student_cnt[n] == 0:
            q.append(n)
            
print(*result)