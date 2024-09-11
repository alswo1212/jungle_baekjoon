from heapq import heapify, heappush, heappop
input()
q = list(map(lambda n : -int(n), input().split()))
heapify(q)
result = 0
while q:
    num1 = -heappop(q)
    num1 -= 1
    if q:
        num2 = -heappop(q)
        num2 -= 1
        if num2 > 0:
            heappush(q, -num2)
    if num1 > 0:
        heappush(q, -num1)
    result += 1

print(-1 if result > 1440 else result)