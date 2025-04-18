def solution(triangle):
    for i in range(1, len(triangle)):
        n = len(triangle[i])
        for j in range(n):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == n-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])