N = int(input())
cards = list(map(int, input().split()))
memo = [*cards]

for i in range(N):
    left, right = 0, i - 1
    while left <= right:
        memo[i] = max(memo[i], cards[left] + memo[right])
        left += 1
        right -= 1

print(memo[-1])