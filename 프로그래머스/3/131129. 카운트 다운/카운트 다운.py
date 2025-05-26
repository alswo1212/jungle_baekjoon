def solution(target):
    l = target + 1
    memo = [[0,0] for _ in range(100_001)]
    nums = []
    for i in range(1,21):
        memo[i][0] = 1
        memo[i][1] = 1
        nums.append(i)
    for i in range(1,21):
        if memo[i*2][0] != 1:
            memo[i*2][0] = 1
            memo[i*2][1] = 0
            nums.append(i*2)
        if memo[i*3][0] != 1:
            memo[i*3][0] = 1
            memo[i*3][1] = 0
            nums.append(i*3)
    memo[50][0] = 1
    memo[50][1] = 1
    nums.append(50)
    
    for i in range(23, l):
        if memo[i][0] != 0 : continue
        min_shoot = float('inf')
        max_cnt = 0
        for num in nums:
            if i - num < 0: continue
            shoot = memo[num][0] + memo[i-num][0]
            cnt = memo[num][1] + memo[i-num][1]
            if shoot < min_shoot:
                min_shoot, max_cnt = shoot, cnt
            elif shoot == min_shoot and max_cnt < cnt:
                max_cnt = cnt
            
        memo[i][0], memo[i][1] = min_shoot, max_cnt
    
    return memo[target]