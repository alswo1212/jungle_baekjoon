N, M = map(int, input().split())
trees = list(map(int, input().split()))
max_height = max(trees)

left = 0
right = max_height
while left <= right:
    mid = (left + right) >> 1

    tree_sum = 0 
    for tree in trees:
        if tree > mid:
            tree_sum += tree - mid

    if tree_sum < M: right = mid - 1
    elif tree_sum > M: left = mid + 1
    else : 
        right = mid
        break

print(right)