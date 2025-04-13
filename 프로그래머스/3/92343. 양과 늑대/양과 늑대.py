from collections import deque

def solution(info, edges):
    answer = 0

    def child_bits(node:int)->int:
        if memo[node] != -1:
            return memo[node]
        
        result = 0
        for child in graph[node]:
            result |= 1 << child
        memo[node] = result
        return result
    
    graph = [[] for _ in range(len(info))]
    memo = [-1] * len(info)
    for parent, child in edges:
        graph[parent].append(child)
    
    # visit, wolf_cnt, sheep_cnt, can_go_node
    q = deque([(1, 0, 1, child_bits(0))])
    while q:
        visit, wolf_cnt, sheep_cnt, can_go_node =  q.popleft()

        if answer < sheep_cnt:
            answer = sheep_cnt

        i = 0
        temp = can_go_node
        while temp:
            if temp%2:
                bit = 1 << i
                if visit & bit == 0:
                    next_can_go_node = can_go_node | child_bits(i)
                    next_can_go_node ^= bit
                    if info[i]:
                        if wolf_cnt + 1 < sheep_cnt:
                            q.append((visit | bit, wolf_cnt+1, sheep_cnt, next_can_go_node))
                    else:
                        q.append((visit | bit, wolf_cnt, sheep_cnt+1, next_can_go_node))
            temp >>= 1
            i+=1

    return answer