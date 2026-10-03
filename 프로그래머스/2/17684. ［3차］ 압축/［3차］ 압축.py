def solution(msg):
    answer = []
    diction = { c: i+1 for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    idx, next_dict_num = 0, 27
    while idx < len(msg):
        start, end = idx, idx+1
        while end <= len(msg) and msg[start:end] in diction:
            end += 1
        if msg[start:end] not in diction:
            diction[msg[start:end]] = next_dict_num
        next_dict_num += 1
        
        answer.append(diction[msg[start:end-1]])
        idx = end - 1
        
    return answer