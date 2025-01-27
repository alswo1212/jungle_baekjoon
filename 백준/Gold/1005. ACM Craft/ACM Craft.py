from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def get_targets(w:int) -> set:
    targets = set([w])
    q = deque([w])
    while q:
        t = q.popleft()
        for nt in down_tree[t]:
            if nt not in targets:
                targets.add(nt)
                q.append(nt)

    return targets

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    topo = [0] * N
    up_tree = defaultdict(list)
    down_tree = defaultdict(list)
    for _ in range(K):
        a, b = map(int, input().split())
        topo[b-1] += 1
        up_tree[a-1].append(b-1)
        down_tree[b-1].append(a-1)

    W = int(input()) - 1
    targets = get_targets(W)
    
    q = []
    removes = []
    for i in targets:
        if topo[i] == 0:
            heappush(q, (times[i], i))
            removes.append(i)

    for i in removes: targets.remove(i)
    
    result = 0
    while q:
        now_time, t = heappop(q)
        if t == W:
            sys.stdout.write(f'{now_time}\n')
            break
        
        for nt in up_tree[t]:
            if nt in targets:
                topo[nt] -= 1
                if topo[nt] == 0:
                    heappush(q, (now_time + times[nt], nt))
                    removes.append(nt)
        for nt in removes:
            if nt in targets:
                targets.remove(nt)