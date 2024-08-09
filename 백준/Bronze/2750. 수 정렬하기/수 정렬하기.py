import sys

n = int(input())

nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

for n in nums : print(n)