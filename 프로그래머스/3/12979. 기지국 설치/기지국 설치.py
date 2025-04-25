from math import ceil
def solution(n, stations, w):
    spaces = [[0, 0]]
    before_end = 1
    for station in stations:
        if before_end < station - w:
            spaces.append([before_end, station-w-1])
        before_end = station + w + 1
    
    if before_end <= n:
        spaces.append([before_end, n])
    
    return sum(ceil((end - start + 1) / (2*w+1)) for start, end in spaces) - 1