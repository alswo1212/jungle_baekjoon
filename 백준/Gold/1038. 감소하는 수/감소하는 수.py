X = int(input())

combis, stack = [], []
for num in range(9,-1,-1):
    stack.append(num)
    while stack:
        now_num = stack.pop()
        combis.append(now_num)
        for next_num in range((now_num % 10) -1, -1, -1):
            stack.append(now_num * 10 + next_num)

combis.sort()

print(combis[X] if len(combis) > X else -1)