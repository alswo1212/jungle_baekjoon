import sys

n = int(sys.stdin.readline())
circles = []
for _ in range(n):
    x, r = map(int,sys.stdin.readline().split())
    circles.append((x-r, x+r))
circles.append((-float('inf'), float('inf')))
circles.sort(key=lambda c: (c[0],-c[1]))
childs = [[] for _ in range(n)]
stack = [0]

for i in range(1, len(circles)):
    circle = circles[i]
    parent = circles[stack[-1]]
    while parent[1] <= circle[0]:
        stack.pop()
        parent = circles[stack[-1]]
    
    childs[stack[-1]].append(i)
    stack.append(i)

match_cnt = 0
for i in range(len(childs)):
    length = 0

    for j in childs[i]:
        length += circles[j][1] - circles[j][0]

    if length != 0 and length == (circles[i][1] - circles[i][0]):
        match_cnt += 1

print(n + 1 + match_cnt)