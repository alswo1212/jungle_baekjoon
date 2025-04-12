def solution(picks, minerals):
    n = len(minerals)
    answer = 25*n
    info = {"diamond":[1,5,25], "iron":[1,1,5], "stone":[1,1,1]}


    def dfs(idx, cnt, left, current_i):
        nonlocal n, answer
        if idx == n or (not idx%5 and left == [0,0,0]):
            answer = min(answer, cnt)
            return

        mineral = minerals[idx]

        if idx%5: 
            dfs(idx+1, cnt + info[mineral][current_i], left, current_i)
        else:
            for i in range(3):
                if not left[i]: continue
                left[i] -= 1
                dfs(idx+1, cnt + info[mineral][i], left, i)
                left[i] += 1

    dfs(0,0,picks,0)

    return answer