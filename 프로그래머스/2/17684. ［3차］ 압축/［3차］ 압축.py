def solution(msg):
    answer = []
    index = {}
    next_idx = 1
    for i in range(26):
        index[chr(65+i)] = next_idx
        next_idx += 1
    
    i = 0
    while i < len(msg):
        l = 1
        while i+l <= len(msg) and msg[i:i+l] in index:
            l += 1
        if msg[i:i+l] not in index:
            index[msg[i:i+l]] = next_idx
            next_idx += 1
        
        answer.append(index[msg[i:i+l-1]])
        i += l-1
            
    return answer