def solution(e, starts):
    nums = [1] * (e+1)
    for i in range(2, e+1):
        for j in range(i, e+1, i):
            nums[j] += 1
    
    memo = [0] * (e+1)
    memo[e] = e
    max_cnt = nums[e]
    for i in range(e-1, 0, -1):
        if nums[i] >= max_cnt:
            memo[i] = i
            max_cnt = nums[i]
        else:
            memo[i] = memo[i+1]
    
    return [memo[s] for s in starts]