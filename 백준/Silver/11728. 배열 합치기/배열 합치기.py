input()
arr = list(map(int, input().split())) + list(map(int, input().split()))
arr.sort()
print(*arr)