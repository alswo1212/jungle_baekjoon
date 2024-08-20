import sys
input = sys.stdin.readline

def histogram(N, arr:list):
    stack = []
    answer = 0
    arr.append(0)

    for i in range(N+1):
        value = arr[i]
        start = i
        while stack and stack[-1][1] >= value :
            start, height = stack.pop()
            answer = max(answer, (i-start)*height)
        stack.append([start, value])
    
    print(answer)

while True :
    read = list(map(int,input().split(' ')))
    N = read[0]
    if N == 0 : break
    histogram(N, read[1:])