from heapq import heappop, heappush
from collections import defaultdict

def solution(operations):
    max_hq, min_hq = [], []
    max_remove, min_remove = defaultdict(int), defaultdict(int)
    for oper in operations:
        comm, data = oper.split(' ')
        data = int(data)
        if comm == 'I':
            heappush(max_hq, -data)
            heappush(min_hq, data)
        elif comm == 'D':
            if data == 1:
                while max_hq:
                    if min_remove[-max_hq[0]]:
                        min_remove[-max_hq[0]] -= 1
                        heappop(max_hq)
                        continue
                    max_remove[-heappop(max_hq)] += 1
                    break
            else:
                while min_hq:
                    if max_remove[min_hq[0]]:
                        max_remove[min_hq[0]] -= 1
                        heappop(min_hq)
                        continue
                    min_remove[heappop(min_hq)] += 1
                    break
    while max_hq and min_remove[-max_hq[0]]:
        min_remove[-heappop(max_hq)] -= 1
    while min_hq and max_remove[min_hq[0]]:
        max_remove[heappop(min_hq)] -= 1
    
    if len(max_hq) == 0 or len(min_hq) == 0:
        return [0,0]
    return [-max_hq[0],min_hq[0]]