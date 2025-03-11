from collections import defaultdict
def solution(orders, course):
    answer = []
    want_lens = set(course)
    counter = defaultdict(int)
    for order in orders:
        order = sorted(order)
        for bits in range(1 << len(order)):
            bit_cnt = 0
            set_menu = ''
            i = 0
            while bits:
                if bits%2:
                    set_menu += order[i]
                    bit_cnt += 1
                bits >>= 1
                i+=1
            if bit_cnt not in want_lens:
                continue
            counter[set_menu] += 1
    
    popular_set = defaultdict(list)
    max_cnt = defaultdict(int)
    for set_menu, cnt  in counter.items():
        if cnt < 2:
            continue
        
        n = len(set_menu)
        if max_cnt[n] < cnt:
            popular_set[n] = [set_menu]
            max_cnt[n] = cnt
        elif max_cnt[n] == cnt:
            popular_set[n].append(set_menu)
    
    for arr in popular_set.values(): answer.extend(arr)
    answer.sort()

    return answer