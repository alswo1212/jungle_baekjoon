from itertools import combinations
from collections import defaultdict

def solution(orders:list[str], course:list[int]):
    answer = []
    for length in course:
        counter = defaultdict(int)
        for order in orders:
            for menus in combinations(sorted(order), length):
                counter[menus] += 1
                
        max_count = 2
        temp = []
        for menus, count in counter.items():
            if count > max_count:
                temp.clear()
                temp.append(''.join(menus))
                max_count = count
            elif count == max_count:
                temp.append(''.join(menus))
        answer += temp
        
    answer.sort()
    return answer