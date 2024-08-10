N, M = map(int,input().split())

nums = list(map(int, input().split()))
visit = [False] *  len(nums)
selected = [0] * 3
result = 0

def make_combi(selected, cnt):
    if cnt == 3:
        global result
        made = sum(selected)
        if made > result and made <= M: result = made
        return
    
    for i in range(len(nums)):
        if visit[i] : continue

        visit[i] = True
        selected[cnt] = nums[i]
        make_combi(selected, cnt+1)
        visit[i] = False

make_combi(selected, 0)

print(result)