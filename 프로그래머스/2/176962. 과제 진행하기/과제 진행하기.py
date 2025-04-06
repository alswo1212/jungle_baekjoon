def solution(plans):
    def time_2_int(time:str)->int:
        return int(time[:2]) * 60 + int(time[3:])
    answer = []
    stack = []
    plans.sort(key=lambda p:time_2_int(p[1]))
    now = time_2_int(plans[0][1])
    for plan in plans:
        plan[1], plan[2] = time_2_int(plan[1]), int(plan[2])
        while stack and plan[1] > now:
            name, need_time = stack.pop()
            play_time = min(plan[1] - now, need_time)
            now += play_time
            if need_time - play_time != 0:
                stack.append((name, need_time - play_time))
            else:
                answer.append(name)
        stack.append((plan[0], plan[2]))
        if now < plan[1]:
            now = plan[1]

    answer.extend(list(map(lambda p: p[0], stack[::-1])))
    return answer