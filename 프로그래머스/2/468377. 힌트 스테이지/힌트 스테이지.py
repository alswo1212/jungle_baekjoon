def solution(cost, hint):
    answer=0
    hint.append([0,0])
    N=len(cost)
    def search(cost_used, now_hints, n):
        if n==N:
            return cost_used
        ncost = cost_used + cost[n][min(now_hints[n], len(cost[n])-1)]
        rt = search(ncost, now_hints, n+1)
        hc, *hints = hint[n]
        ncost+=hc
        for h in hints:
            now_hints[h-1]+=1
        rt=min(rt, search(ncost, now_hints, n+1))
        for h in hints:
            now_hints[h-1]-=1
        return rt

    return search(0, [0]*N,0)