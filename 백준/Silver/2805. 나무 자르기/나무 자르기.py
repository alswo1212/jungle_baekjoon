N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
while left <= right:
    mid = (left + right) >> 1

    tree_sum = sum(tree - mid for tree in trees if tree > mid)

    if tree_sum < M: right = mid - 1
    elif tree_sum > M: left = mid + 1
    else : 
        right = mid
        break

print(right)