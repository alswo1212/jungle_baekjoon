import sys

V, E = map(int,input().split())

lines = []
for _ in range(E):
    a, b, c = map(int,sys.stdin.readline().split())
    lines.append((a,b,c))

lines.sort(key=lambda l: l[2])
result = 0
start_p = [i for i in range(V+1)]

def get_start_p(p):
    return p if start_p[p] == p else get_start_p(start_p[p])

for line in lines:
    start, to, length = line
    s_p1 = get_start_p(start)
    s_p2 = get_start_p(to)
    if s_p1 == s_p2: continue
    
    if s_p1 < s_p2:
        start_p[s_p2] = s_p1
    else :
        start_p[s_p1] = s_p2
    result += length

print(result)