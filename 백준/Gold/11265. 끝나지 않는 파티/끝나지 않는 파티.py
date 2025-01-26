import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().split())
edges =[list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        if k == i:
            continue
        for j in range(N):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

OK = "Enjoy other party"
NO = "Stay here"
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    result = OK if edges[A][B] <= C else NO
    print(f'{result}\n')