def solution(routes):
    answer = 0
    routes.sort(key=lambda r: r[::-1])
    now = -30_001
    for start, end in routes:
        if start > now:
            now = end
            answer += 1
    return answer