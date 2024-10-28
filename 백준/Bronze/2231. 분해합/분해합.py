N = int(input())
min_constructor = N

cnt = 1
while min_constructor > 0:
    cnt += 1
    min_constructor //= 10

min_constructor = N
start = max(N - cnt * 10, 0)
for i in range(start, N):
    val = i
    temp = i
    while temp > 0:
        val += temp % 10
        temp //= 10
    if val == N:
        min_constructor = i
        break
    
print(0 if min_constructor == N else min_constructor)
