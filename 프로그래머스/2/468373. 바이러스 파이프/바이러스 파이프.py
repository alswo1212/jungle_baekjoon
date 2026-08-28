from collections import deque
def get_cases(types:list[int], k:int):
    cases = [[0] * k]
    
    def make_case(ignore_idx:int, cur_idx:int):
        if cur_idx == k:
            cases.append([*cases[-1]])
            return
        
        for i, type in enumerate(types):
            if ignore_idx == i: 
                continue
            cases[-1][cur_idx] = type
            make_case(i, cur_idx+1)
            
    make_case(-1, 0)
    return cases[:-1]

def bfs(tree:list[tuple], start_node:int, open_order:list[int], pipe_types:list[int]):
    blocked_node = { type: [] for type in pipe_types }
    q = deque([start_node])
    visit = set()
    
    for open_type in open_order:
        while blocked_node[open_type]:
            q.append(blocked_node[open_type].pop())

        while q:
            cur_node = q.popleft()
            visit.add(cur_node)

            for node, type in tree[cur_node]:
                if node in visit: 
                    continue
                if type != open_type:

                    blocked_node[type].append(node)
                    continue
                q.append(node)

    return len(visit)
        

def solution(n, infection, edges, k):
    answer = 0
    pipe_types = [1,2,3]
    cases = get_cases(pipe_types, k)
    tree = [[] for _ in range(n+1)]
    for node1, node2, type in edges:
        tree[node1].append((node2, type))
        tree[node2].append((node1, type))

    for case in cases:
        answer = max(bfs(tree, infection, case, pipe_types), answer)
        
    return answer