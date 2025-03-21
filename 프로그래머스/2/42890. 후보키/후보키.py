def solution(relation):
    def check_miniality(bit):
        for i in range(len(candi_bits)):
            can = candi_bits[i]
            temp = can | bit
            if temp == bit:
                return False
            elif temp == can:
                candi_bits[i] = bit
                return True
        return True
    
    def check_uniqueness(idxs):
        distinct = set()
        for row in relation:
            distinct.add(''.join(map(lambda i: row[i], idxs)))
        return len(distinct) == n
    
    n, m = len(relation), len(relation[0])
    candi_bits = []
    for combi in range(1, 1<<m):
        if not check_miniality(combi):
            continue
        
        use_idxs = []
        i, temp = 0, combi
        while combi:
            if combi % 2:
                use_idxs.append(i)
            i += 1
            combi >>= 1
        
        if check_uniqueness(use_idxs):
            candi_bits.append(temp)
    
    return len(candi_bits)