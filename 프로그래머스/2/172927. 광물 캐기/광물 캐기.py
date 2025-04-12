def solution(picks, minerals):
    answer = 0
    arr = [i for i in range(len(picks)) for j in range(picks[i])]
    N, M = len(minerals), len(arr)
    axes = [
        {"diamond": 1, 'iron':1, 'stone':1}, 
        {"diamond": 5, 'iron':1, 'stone':1}, 
        {"diamond": 25, 'iron':5, 'stone':1}
        ]

    cnt, i = 0, 0
    bundles = []
    while cnt < M and i < N:
        next_i = min(i+5, N)
        bundles.append(minerals[i:next_i])
        i = next_i
        cnt += 1
    
    bundles.sort(key=lambda b: sum(axes[2][m] for m in b), reverse=True)
    for i in range(len(bundles)):
        answer += sum(axes[arr[i]][m] for m in bundles[i])

    return answer