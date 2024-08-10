result_min = 10 ** 9
result_max = -(10 ** 9)

n = int(input())

nums = list(map(int, input().split()))
oper_cnts = list(map(int, input().split()))

def calc(depth, calced):
    if depth == n:
        global result_min, result_max
        result_min = min(result_min, calced)
        result_max = max(result_max, calced)
        return
    
    for i in range(4):
        if oper_cnts[i] == 0 : continue

        oper_cnts[i] -= 1

        if i == 0: calc(depth+1, calced + nums[depth])
        elif i == 1: calc(depth+1, calced - nums[depth])
        elif i == 2: calc(depth+1, calced * nums[depth])
        else :
            if calced * nums[depth] < 0 :
                calc(depth+1, -(abs(calced) // abs(nums[depth])))
            else :
                calc(depth+1, calced // nums[depth])

        oper_cnts[i] += 1

calc(1, nums[0])

print(result_max, result_min, sep='\n')