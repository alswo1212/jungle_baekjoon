def solution(k, ranges):
    answer = []
    heights = [k]
    areas = []
    while heights[-1] != 1:
        if heights[-1] % 2:
            heights.append(heights[-1]*3+1)
        else:
            heights.append(heights[-1]>>1)
        
        y1, y2 = heights[-2], heights[-1]
        if y1 < y2:
            areas.append(y1 + (y2-y1)/2)
        else:
            areas.append(y1 - (y1-y2)/2)
    
    MAX = sum(areas)
    n = len(areas)
    for start, end in ranges:
        if start > n+end:
            result = -1
        else:
            result = MAX - sum(areas[:start]) - (sum(areas[end:]) if end else 0)
        answer.append(result)

    return answer