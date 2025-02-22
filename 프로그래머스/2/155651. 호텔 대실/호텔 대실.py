def solution(book_time):
    def time_2_int(t:str)->int:
        h, m = map(int, t.split(':'))
        return h*60 + m
    
    times = [0] * (60 * 24 + 10)
    max_time = 24 * 60 + 60
    for time in book_time:
        start_time = time_2_int(time[0])
        end_time = time_2_int(time[1])
        times[start_time] += 1
        times[min(end_time + 10, max_time)] -= 1

    for i in range(1, len(times)):
        times[i] += times[i-1]
    return max(times)