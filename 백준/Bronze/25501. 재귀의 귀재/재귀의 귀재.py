import sys
input = sys.stdin.readline

count = 0

def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

repeat = int(input())
for _ in range(repeat):
    result = isPalindrome(input().strip())
    print(result, count)
    count = 0