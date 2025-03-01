def solution(sequence, k):
    n = len(sequence)
    answer = [0,0]
    left, right = 0, 0
    sumed = sequence[0]
    max_diff = n
    while left <= right:
        if sumed < k and right+1 < n:
            right += 1
            sumed += sequence[right]
        else:
            sumed -= sequence[left]
            left += 1
        if sumed == k and max_diff > right-left:
            answer[0], answer[1] = left, right
            max_diff = right-left
    return answer