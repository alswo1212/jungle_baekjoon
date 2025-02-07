from collections import defaultdict
from bisect import bisect_left
def get_sums(idx, chooses, dice, temp, result):
    if idx == len(chooses):
        result.append(temp)
        return
    for num in dice[chooses[idx]]:
        get_sums(idx+1, chooses, dice, temp+num, result)

def bit_count(num):
    result = 0
    while num:
        if num % 2 == 1:
            result += 1
        num >>= 1
    return result

def solution(dice):
    n = len(dice)

    ranges = 1 << n
    win_cnt = defaultdict(int)
    for i in range(ranges):
        if bit_count(i) == n // 2:
            choose = [[],[]]
            idx = 0
            while idx < n:
                choose[i % 2].append(idx)
                idx += 1
                i >>= 1
            a, b = [], []
            key = tuple(choose[0])
            get_sums(0, choose[0], dice, 0, a)
            get_sums(0, choose[1], dice, 0, b)
            a.sort()
            b.sort()
            for a_num in a:
                win_cnt[key] += bisect_left(b, a_num)
    max_list = []
    max_num = 0
    for key, win_count in win_cnt.items():
        if win_count > max_num:
            max_num = win_count
            max_list = list(key)
    for i in range(len(max_list)):
        max_list[i] += 1
    return max_list