n = int(input())
arr = [1] * (n + 1)
for i in range(2, n+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 15746
print(arr[n])