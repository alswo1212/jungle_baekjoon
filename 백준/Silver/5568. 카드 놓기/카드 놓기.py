import sys

n = int(input())
k = int(input())

cards = [sys.stdin.readline() for _ in range(n)]
visit = [False] * n
results = set()

def make_mixture(depth:int, mixture:str):
    if depth == k:
        results.add(mixture.replace('\n',''))
        return
    
    for i in range(n):
        if visit[i] : continue

        visit[i] = True
        make_mixture(depth = depth + 1, mixture = mixture + cards[i])
        visit[i] = False

make_mixture(0, '')

print(len(results))