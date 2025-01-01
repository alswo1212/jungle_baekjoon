from collections import defaultdict
from bisect import bisect_left, bisect_right
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnts = defaultdict(int)
for num in arr:
    cnts[num] += 1

visit = set()
result = 0
for i in range(N-1):
    for j in range(i+1, N):
        find_num = arr[i] + arr[j]
        if find_num in visit:
            continue
        if find_num > arr[-1]:
            break

        if arr[i] == arr[j] == 0:
            if cnts[0] > 2:
                # case : 0 + 0, cnts[0] > 2
                result += cnts[0] # 0의 개수 
                visit.add(find_num)
        elif arr[i] == 0 or arr[j] == 0:
            # case : 0 + n, cnts[n] > 2
            target = j if arr[i] == 0 else i
            if cnts[arr[target]] >= 2:
                result += cnts[arr[target]] # n의 개수
                visit.add(find_num)
        else:
            left = bisect_left(arr, find_num)
            right = bisect_right(arr, find_num)
            result += right - left
            visit.add(find_num)

print(result)