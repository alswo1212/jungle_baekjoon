import sys
input = sys.stdin.readline

while True:
    n = input().strip()
    if n == '0': break
    print('yes 'if tuple(n) == tuple(n[::-1]) else 'no')
