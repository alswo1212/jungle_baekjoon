def solution(n, computers):
    n = len(computers)
    nets = [-1] * n
    for i in range(n):
        if nets[i] != -1:
            continue
        stack = [i]
        while stack:
            node = stack.pop()
            nets[node] = i
            for next_node in range(n):
                if computers[node][next_node] == 0:
                    continue
                if nets[next_node] == -1:
                    stack.append(next_node)
    return len(set(nets))