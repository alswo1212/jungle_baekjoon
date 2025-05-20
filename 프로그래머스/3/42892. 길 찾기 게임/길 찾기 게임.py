import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    answer = [[]]
    def preorder(target):
        answer[-1].append(target['id'])
        if target['left']:
            preorder(target['left'])
        if target['right']:
            preorder(target['right'])

    def postorder(target):
        if target['left']:
            postorder(target['left'])
        if target['right']:
            postorder(target['right'])
        answer[-1].append(target['id'])

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
                    target[direc] = node
                    break
                target = target[direc]

    preorder(root)
    answer.append([])
    postorder(root)

    return answer