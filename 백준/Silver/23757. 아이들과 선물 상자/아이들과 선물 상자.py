from heapq import heapify, heappop, heappush
N, M = map(int, input().split())
q = list(map(lambda n: -int(n), input().split()))
children = list(map(int, input().split()))
heapify(q)

for child in children:
    num = -heappop(q)
    if num < child:
        print(0)
        quit()
    heappush(q, -(num - child))

print(1)