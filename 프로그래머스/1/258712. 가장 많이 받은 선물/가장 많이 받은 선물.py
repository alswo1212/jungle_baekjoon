def solution(friends, gifts):
    n = len(friends)
    name_2_idx = {}
    for i in range(n):
        name_2_idx[friends[i]] = i

    edges = [[0] * n for _ in range(n)]
    for gift in gifts:
        y, x = gift.split(' ')
        edges[name_2_idx[y]][name_2_idx[x]] += 1
    
    jisoo = [0] * n
    for i in range(n):
        sand_cnt = sum(edges[i])
        receive_cnt = 0
        for j in range(n):
            receive_cnt += edges[j][i]
        jisoo[i] = sand_cnt - receive_cnt
    
    results = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j : continue
            if edges[i][j] > edges[j][i]:
                results[i] += 1
            elif edges[i][j] == edges[j][i] and jisoo[i] > jisoo[j]:
                results[i] += 1
    
    return max(results)