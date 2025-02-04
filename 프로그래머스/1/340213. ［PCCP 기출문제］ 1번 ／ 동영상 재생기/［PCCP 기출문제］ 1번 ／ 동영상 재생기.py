def solution(video_len, pos, op_start, op_end, commands):
    def time2int(time:str) -> int:
        m, s = map(int, time.split(':'))
        return m * 60 + s
    def int2time(num:int)-> str:
        return f'{num // 60 :0>2}:{num % 60 :0>2}'
    
    now = time2int(pos)
    video_max = time2int(video_len)
    ops = time2int(op_start)
    ope = time2int(op_end)
    if ops <= now <= ope:
        now = ope

    for comm in commands:
        if comm == 'prev':
            now = max(0, now - 10)
        elif comm == 'next':
            now = min(video_max, now + 10)
        if ops <= now <= ope:
            now = ope

    return int2time(now)