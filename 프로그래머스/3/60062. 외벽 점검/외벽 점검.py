from itertools import permutations
def solution(n, weak, dist):
    N, M = len(weak), len(dist)
    goal = (1 << N) - 1

    memo_bits = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            bit = 0
            d = dist[i]
            idx = j
            while d >= 0:
                bit |= 1 << idx
                idx = (idx + 1) % N
                temp = weak[idx] - weak[idx-1]
                if temp < 0:
                    temp += n
                d -= temp
            if bit == goal:
                return 1
            memo_bits[i][j] = bit
    
    for cnt in range(1, M+1):
        for permu in permutations(range(M), cnt):
            for start in range(N):
                bits = 0
                for idx in permu:
                    bits |= memo_bits[idx][start]
                    start =  (start + bin(memo_bits[idx][start])[2:].count('1')) % N
                if bits == goal:
                    return cnt

    return -1