def rel_2_value(row:list[str], use_bit:int):
    answer = ''
    idx = 0
    while use_bit:
        if use_bit & 1:
            answer += row[idx]
        idx += 1
        use_bit >>= 1
    return answer

def valid_minimality(candidate_keys:list[int], target_bit:int):
    for key_use in candidate_keys:
        if key_use & target_bit == key_use:
            return False
    return True

def solution(relation:list[list[str]]):
    N, M = len(relation), len(relation[0])
    candidate_keys = []

    for bit in range(0, 1 << M):
        if not valid_minimality(candidate_keys, bit): continue

        if len(set(map(lambda r: rel_2_value(r, bit), relation))) == N:
            candidate_keys.append(bit)

    return len(candidate_keys)