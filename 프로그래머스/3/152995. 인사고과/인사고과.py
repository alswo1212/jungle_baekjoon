def solution(scores):
    n = len(scores)
    people = [(scores[i][0], scores[i][1], i) for i in range(n)]
    people.sort(key=lambda p : (-p[0], p[1]))
    filterd = []
    max_val1, max_val2 = people[0][0], people[0][1]
    wanho = 0
    for p in people:
        if p[0] < max_val1 and p[1] < max_val2:
            continue
        if p[0] > max_val1 or p[1] > max_val2:
            max_val1, max_val2 = p[0], p[1]
        filterd.append((p[0]+p[1], p[2]))
        if p[2] == 0:
            wanho = p[0] + p[1]
    filterd.sort(reverse=True)
    
    cnt = 0
    for i in range(len(filterd)):
        score, id = filterd[i][0], filterd[i][1]
        if wanho < score:
            cnt += 1
        if id == 0:
            return cnt + 1

    return -1