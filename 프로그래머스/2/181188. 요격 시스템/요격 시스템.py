def solution(targets):
    answer = 0
    targets.sort(key=lambda t : t[1])
    right = 0
    for t in targets:
        if t[0] >= right:
            answer += 1
            right = t[1]
    return answer