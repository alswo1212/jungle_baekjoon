def solution(players, m, k):
    l = len(players)
    server_cnt, scale_out_cnt = [0] * l, [0] * l
    for i in range(l):
        p = players[i]
        scale_out = max(p // m - server_cnt[i], 0)
        if scale_out:
            scale_out_cnt[i] = scale_out
            for j in range(i, min(l, i+k)):
                server_cnt[j] += scale_out
        
    return sum(scale_out_cnt)