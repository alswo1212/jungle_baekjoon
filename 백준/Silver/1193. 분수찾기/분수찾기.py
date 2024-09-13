X = int(input())
def solv(is_odd, cnt, seq):
    return f'{cnt + 1 - seq}/{seq}' if is_odd else f'{seq}/{cnt + 1 - seq}'

cnt = 1
while X > cnt:
    X -= cnt
    cnt += 1
print(solv(cnt % 2, cnt, X))