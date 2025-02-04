def solution(diffs, times, limit):
    answer = max(diffs)
    def calc(level:int)->int:
        need_time = times[0]
        for i in range(1, len(diffs)):
            diff = diffs[i] 
            time_cur, time_prev = times[i], times[i-1]
            if diff <= level:
                need_time += time_cur
            else:
                repeat = diff - level
                need_time += repeat * (time_cur + time_prev) + time_cur
        return need_time
    
    left, right = 1, answer
    while left <= right:
        mid = (left + right) >> 1
        time = calc(mid)
        if time <= limit:
            right = mid - 1
            answer = min(answer, mid)
        else :
            left = mid + 1

    return answer
