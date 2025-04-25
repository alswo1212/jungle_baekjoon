def solution(A, B):
    answer = 0
    i, j = 0, 0
    a_len, b_len = len(A), len(B)
    A.sort()
    B.sort()
    while i < a_len and j < b_len:
        if A[i] < B[j]:
            i += 1
            j += 1
            answer += 1
        else:
            j += 1
            
    return answer