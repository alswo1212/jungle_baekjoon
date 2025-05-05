import sys
sys.setrecursionlimit(10**6)
def solution(tickets):
    answer = []
    edges = {}
    for s, e in tickets:
        if s not in edges:
            edges[s] = []
        edges[s].append(e)

    n = len(tickets) + 1
    def dfs(arr:list, cnt:dict):
        if len(arr) == n:
            answer.append(arr)
            return
        
        now_node = arr[-1]
        if now_node in cnt:
            for node in cnt[now_node]:
                next_cnt = cnt.copy()
                next_cnt[now_node] = next_cnt[now_node].copy()
                next_cnt[now_node].remove(node)
                dfs([*arr, node], next_cnt)

    dfs(['ICN'], edges)
    answer.sort()
    return answer[0]