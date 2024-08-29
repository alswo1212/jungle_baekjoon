import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a,b,c = map(int, input().split())
    cnt = 0
    for i in range(a):
        for j in range(b):
            for k in range(c):
                if (i+1) % (j+1) == (j+1) % (k+1) == (k+1) % (i+1):
                    cnt += 1
    print(cnt)