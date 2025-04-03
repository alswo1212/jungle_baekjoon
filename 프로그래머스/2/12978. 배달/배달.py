def solution(N, road, K):
    graph = [[float('inf')] * N for _ in range(N)]
    for n1, n2, t in road:
        if graph[n1-1][n2-1] > t:
            graph[n1-1][n2-1] = t
            graph[n2-1][n1-1] = t
    for i in range(N):
        graph[i][i] = 0
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    return len(list(filter(lambda t: t <= K, graph[0])))