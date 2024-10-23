import sys
input = sys.stdin.readline

input()
s = input().strip()
print(sum(int(c) for c in s))