def solution(e, starts):
    answer = []
    nums = [0] * (e+1)
    for i in range(1, int(e ** 0.5) +1):
        nums[i*i] += 1
        for j in range(i+1, e// i + 1):
            nums[i*j] += 2
    
    memo = [0] * (e+1)
    memo[e] = e
    max_cnt = nums[e]
    for i in range(e-1, 0, -1):
        if nums[i] >= max_cnt:
            memo[i] = i
            max_cnt = nums[i]
        else:
            memo[i] = memo[i+1]
    for s in starts:
        answer.append(memo[s])
    
    return answer