def solution(n, times):
    left, right = 1, max(times) * n
    while left <= right:
        mid = left + (right - left) // 2
        temp = sum(mid // t for t in times)
        if temp < n:
            left = mid+1
        else:
            right = mid-1
    return left