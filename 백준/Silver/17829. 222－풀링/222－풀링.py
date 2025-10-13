import sys
input = sys.stdin.readline

def CNN_222(metric:list[list[int]]) -> int:
    if len(metric) == 1:
        return metric[0][0]
    
    l = len(metric)
    next_metric = [[0] * (l>>1) for _ in range(l>>1)]
    temp = [0] * 4
    for i in range(0, l, 2):
        for j in range(0, l, 2):
            temp[0], temp[1], temp[2], temp[3] = metric[i][j], metric[i+1][j], metric[i][j+1], metric[i+1][j+1]
            temp.sort()
            next_metric[i>>1][j>>1] = temp[-2]
    
    return CNN_222(next_metric)

N = int(input())

metric = [list(map(int, input().split())) for _ in range(N)]
print(CNN_222(metric))