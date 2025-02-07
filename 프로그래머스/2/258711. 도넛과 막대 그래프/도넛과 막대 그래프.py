from collections import defaultdict
def check_graph(start, graph):
    stack = [start]
    duple_cnt = 0
    bundle = set()
    
    while stack:
        node = stack.pop()
        if node in bundle:
            duple_cnt += 1
        bundle.add(node)
        nexts = graph[node]
        while nexts:
            stack.append(nexts.pop())

    if duple_cnt >= 2:
        return 3
    elif duple_cnt == 0:
        return 2
    return 1

def solution(edges):
    answer = [0,0,0,0]
    graph = defaultdict(list)
    in_cnt = defaultdict(int)
    for start, to in edges:
        graph[start].append(to)
        in_cnt[to] += 1

    added_node = 0
    graph[0]
    for node, out_lines in graph.items():
        if len(out_lines) > len(graph[added_node]):
            added_node = node
        elif len(out_lines) == len(graph[added_node]) and in_cnt[node] < in_cnt[added_node]:
            added_node = node
    answer[0] = added_node

    for node in graph[added_node]:
        answer[check_graph(node,graph)] += 1

    return answer