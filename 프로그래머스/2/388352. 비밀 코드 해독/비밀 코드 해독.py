from itertools import combinations
def solution(n, q, ans):
    answer = 0
    q = list(map(set, q))
    def is_candi(s)->bool:
        for i in range(len(q)):
            if len(s & q[i]) != ans[i]:
                return False
        return True
    
    for combi in combinations(range(1, n+1), 5):
        if is_candi(set(combi)):
            answer += 1
    return answer