from collections import deque
def solution(a, edges):
    links = [set() for _ in range(len(a))]
    for i in range(len(edges)):
        to, start = edges[i]
        links[start].add(to)
        links[to].add(start)
    
    q = deque()
    for i in range(len(links)):
        if len(links[i]) == 1:
            q.append(i)

    answer = 0
    root = -1
    while q:
        idx = q.popleft()
        if len(links[idx]) == 0:
            root = idx
            break
        parent = links[idx].pop()
        temp = a[idx]
        a[idx] -= temp
        a[parent] += temp
        answer += abs(temp)
        links[parent].remove(idx)
        if len(links[parent]) == 1:
            q.append(parent)
    
    return -1 if a[root] != 0 else answer