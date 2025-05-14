def solution(a):
    n = len(a)
    if n <= 2:
        return n
    answer = 2
    left_min, right_min = [float('inf')]+a[:-1], a[1:]+[float('inf')]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], left_min[i])
        right_min[n-i-1] = min(right_min[n-i], right_min[n-i-1])
    
    for i in range(1, n-1):
        if a[i] < left_min[i] or a[i] < right_min[i]:
            answer += 1
    
    return answer