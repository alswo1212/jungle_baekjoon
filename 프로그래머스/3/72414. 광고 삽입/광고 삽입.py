def solution(play_time, adv_time, logs):
    def time_2_int(time:str)->int:
        return int(time[:2]) * 60 * 60 + int(time[3:5]) * 60 + int(time[6:])
    def int_2_time(num:int)->str:
        hh = num // (60*60)
        num %= (60*60)
        mm = num // 60
        ss = num % 60
        return f'{hh:02}:{mm:02}:{ss:02}'
    
    cnts = [0] * (time_2_int(play_time) + 1)
    for t in logs:
        times = t.split('-')
        cnts[time_2_int(times[0])] += 1
        cnts[time_2_int(times[1])] -= 1
    for i in range(1, len(cnts)):
        cnts[i] += cnts[i-1]

    left, right = 0, time_2_int(adv_time)
    answer = 0
    max_sum = 0
    temp_sum = sum(cnts[:right])
    for i in range(right, len(cnts)):
        if temp_sum > max_sum:
            max_sum = temp_sum
            answer = left
        temp_sum += cnts[i]
        temp_sum -= cnts[left]
        left += 1
    
    return int_2_time(answer)