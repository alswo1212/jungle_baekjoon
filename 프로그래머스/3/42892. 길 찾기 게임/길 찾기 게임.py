def solution(nodeinfo):
    answer = [[]]
    nodes = {}
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        if y not in nodes:
            nodes[y] = []
        nodes[y].append({
            'num':x, 'left': None, 'right':None, 'id':i+1
        })

    keys = list(nodes.keys())
    keys.sort(reverse=True)
    root = nodes[keys[0]][0]
    for k in keys[1:]:
        for node in nodes[k]:
            target = root
            while target:
                direc = 'right' if target['num'] < node['num'] else 'left'
                if not target[direc]:
                    target.__setitem__(direc, node)
                    break
                target = target[direc]

    stack = [root]
    while stack:
        target = stack.pop()
        answer[-1].append(target['id'])
        if target['right']:
            stack.append(target['right'])
        if target['left']:
            stack.append(target['left'])

    answer.append([])

    stack = [root]
    t_stack= []
    while stack:
        target = stack.pop()
        t_stack.append(target)
        if target['left']:
            stack.append(target['left'])
        if target['right']:
            stack.append(target['right'])
    while t_stack:
        answer[-1].append(t_stack.pop()['id'])

    return answer