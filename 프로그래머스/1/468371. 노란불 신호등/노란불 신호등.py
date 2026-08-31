def solution(signals):
    answer = -1
    target_len = 1
    for seconds in signals:
        target_len *= sum(seconds)
    flag_arr = [0] * target_len
    target = len(signals)
    
    for sigs in signals:
        i = 0
        while i < target_len:
            for sigs_idx, num in enumerate(sigs):
                if i >= target_len: break
                
                flag = 1 if sigs_idx == 1 else 0
                for _ in range(num):
                    if i >= target_len: break
                    
                    flag_arr[i] += flag
                    i += 1
    
    for i in range(target_len):
        if flag_arr[i] == target:
            answer = i+1
            break
        
    return answer