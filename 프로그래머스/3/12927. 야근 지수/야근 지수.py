def solution(n, works):
    works = sorted(works, reverse=True)
    while n and works[0]:
        temp = works[0]
        i = 0
        while n and i < len(works) and temp == works[i]:
            works[i] -= 1
            i+=1
            n -= 1
    return sum(work * work for work in works)