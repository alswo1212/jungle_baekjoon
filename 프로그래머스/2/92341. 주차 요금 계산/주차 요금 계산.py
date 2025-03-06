from collections import defaultdict
from math import ceil
def solution(fees, records):
    def time_2_int(time:str)->int:
        return int(time[:2]) * 60 + int(time[3:])
    answer = []
    max_time = 24*60-1
    parking_lot = defaultdict(list)
    for record in records:
        time, car_num, div = record.split(' ')
        parking_lot[car_num].append(time_2_int(time))
    
    cars = list(parking_lot.keys())
    cars.sort()
    
    for car in cars:
        car_times = parking_lot[car]
        if len(car_times) % 2 == 1:
            car_times.append(max_time)
        
        parking_time = 0
        while car_times:
            out_time, in_time = car_times.pop(), car_times.pop()
            parking_time += out_time - in_time
        
        if parking_time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ceil((parking_time-fees[0])/fees[2]) * fees[3])

    return answer