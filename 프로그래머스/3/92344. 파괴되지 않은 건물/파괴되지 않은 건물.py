def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    reduce = [[0] * M for _ in range(N)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        reduce[r1][c1] += degree
        if r2+1 < N:
            reduce[r2+1][c1] -= degree
        if c2+1 < M:
            reduce[r1][c2+1] -= degree
        if r2+1 < N and c2+1 < M:
            reduce[r2+1][c2+1] += degree

    for i in range(N):
        for j in range(1, M):
            reduce[i][j] += reduce[i][j-1]
    for i in range(N):
        for j in range(M):
            if i > 0:
                reduce[i][j] += reduce[i-1][j]
            if board[i][j] + reduce[i][j] > 0:
                answer += 1
    return answer