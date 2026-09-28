def rel_2_value(row:list[str], use_bit:int):
    answer = ''
    idx = 0
    while use_bit:
        if use_bit & 1:
            answer += row[idx]
        idx += 1
        use_bit >>= 1
    return answer

def valid_minimality(candidate_keys:list[int], bit_cnt:int, target_bit:int):
    for cnt in range(bit_cnt):
        for key_use in candidate_keys[cnt]:
            if key_use & target_bit == key_use:
                return False
    return True

def solution(relation:list[list[str]]):
    N, M = len(relation), len(relation[0])
    key_bits = [[] for _ in range(M+1)]
    candidate_keys = [[] for _ in range(M+1)]

    for bit in range(0, 1 << M):
        key_bits[bin(bit).count('1')].append(bit)

    for bit_cnt, bits in enumerate(key_bits):
        for bit in bits:
            if not valid_minimality(candidate_keys, bit_cnt, bit): continue

            if len(set(map(lambda r: rel_2_value(r, bit), relation))) == N:
                candidate_keys[bit_cnt].append(bit)

    return sum(map(len, candidate_keys))