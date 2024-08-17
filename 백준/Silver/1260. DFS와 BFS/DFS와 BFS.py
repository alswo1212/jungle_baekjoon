import sys
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())

num_dict = {}

for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    if num1 not in num_dict:
        num_dict[num1] = {
            'dfs_used' : False,
            'bfs_used' : False,
            'link' : []
        }
    num_dict[num1]['link'].append(num2)

    if num2 not in num_dict:
        num_dict[num2] = {
            'dfs_used' : False,
            'bfs_used' : False,
            'link' : []
        }
    num_dict[num2]['link'].append(num1)

stack = [V]
dfs_result = []
while stack:
    poped = stack.pop()
    if poped not in num_dict:
        dfs_result.append(poped)
        continue

    if not num_dict[poped]['dfs_used']:
        dfs_result.append(poped)
        num_dict[poped]['dfs_used'] = True
        
    num_dict[poped]['link'].sort()
    for num in num_dict[poped]['link'][::-1]:
        if num_dict[num]['dfs_used'] : continue
        stack.append(num)

print(*dfs_result)

q = deque([V])
bfs_result = []
while q:
    polled = q.popleft()
    if polled not in num_dict:
        bfs_result.append(polled)
        continue

    if not num_dict[polled]['bfs_used']:
        bfs_result.append(polled)
        num_dict[polled]['bfs_used'] = True
    
    for num in num_dict[polled]['link']:
        if num_dict[num]['bfs_used']: continue
        q.append(num)

print(*bfs_result)