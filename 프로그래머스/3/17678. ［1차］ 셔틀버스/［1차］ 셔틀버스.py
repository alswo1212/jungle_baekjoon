from collections import deque
def solution(n, t, m, timetable):
    def time_2_int(time:str)->int:
        return int(time[:2]) * 60 + int(time[3:])
    def int_2_timme(time:int)->str:
        return f'{time//60 :02}:{time%60 :02}'
    
    start = 9 * 60
    arrs = []
    times = deque(sorted(map(time_2_int, timetable)))
    for _ in range(n):
        arrs.append((start, []))
        cnt = m
        while cnt and times:
            if times[0] > start:
                break
            cnt -= 1
            arrs[-1][1].append(times.popleft())
        start += t
    
    if len(arrs[-1][1]) == 0:
        answer = arrs[-1][0]
    elif len(arrs[-1][1]) == m:
        answer = arrs[-1][1][-1] - 1
    else:
        answer = arrs[-1][0]
        
    return int_2_timme(answer)