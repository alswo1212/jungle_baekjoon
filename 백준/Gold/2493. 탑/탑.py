n = int(input())
arr = list(map(int, input().split()))
heights = []
result = []
for i in range(n):
    if len(heights) == 0:
        heights.append(i)
        result.append(0)
        continue

    temp = 0
    while len(heights) != 0:
        if arr[heights[-1]] <= arr[i]:
            heights.pop()
            continue
        temp = heights[-1] + 1
        break

    result.append(temp)
    heights.append(i)

print(*result)