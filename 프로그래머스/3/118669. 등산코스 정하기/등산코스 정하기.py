from heapq import heappush, heappop
from collections import defaultdict
def solution(n, paths, gates, summits):
    answer = [float('inf'), float('inf')]
    loads = defaultdict(list)
    for i, j, w in paths:
        loads[i].append((j,w))
        loads[j].append((i,w))
    gates = set(gates)
    summits = set(summits)

    def bfs(start:int):
        visit = defaultdict(int)
        q = [(0, start)]
        while q:
            intensity, node = heappop(q)
            if intensity > answer[1]:
                return
            if node in gates:
                if intensity < answer[1]:
                    answer[1], answer[0] = intensity, start
                elif intensity == answer[1] and start < answer[0]:
                    answer[0] = start
                break
            
            for next_node, w in loads[node]:
                if visit[next_node] != 0 and visit[next_node] <= w:
                    continue
                if next_node in summits:
                    continue
                visit[next_node] = w
                heappush(q, (max(w, intensity), next_node))
        
    for summit in summits:
        bfs(summit)
    return answer