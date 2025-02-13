def solution(m, n, startX, startY, balls):
    def calc(y1, x1, y2, x2):
        result = float('inf')
        if x1 - x2 != 0:
            result = min(result, abs(x1-x2)**2 + (y1+y2)**2)
            result = min(result, abs(x1-x2)**2 + (n-y1+n-y2)**2)
        else:
            if y1 < y2:
                result = min(result, (y1+y2)**2)
            else:
                result = min(result, (n-y1+n-y2)**2)
        if y1 - y2 != 0:
            result = min(result, (x1+x2)**2 + abs(y1-y2)**2)
            result = min(result, (m-x1+m-x2)**2 + abs(y1-y2)**2)
        else:
            if x1 < x2:
                result = min(result, (x1+x2)**2)
            else:
                result = min(result, (m-x1+m-x2)**2)

        return result
    answer = []
    for x, y in balls:
        answer.append(calc(startY, startX, y, x))
    return answer