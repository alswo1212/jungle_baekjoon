import sys
N = int(input())
tree = {}

for _ in range(N):
    root, l_node, r_node = input().split()
    tree[root] = [l_node, r_node]

def preorder(target):
    if target == '.':
        return
    sys.stdout.write(target)
    
    preorder(tree[target][0])
    preorder(tree[target][1])
    

def inorder(target):
    if target == '.':
        return
    inorder(tree[target][0])
    sys.stdout.write(target)
    inorder(tree[target][1])

def postorder(target):
    if target == '.':
        return
    postorder(tree[target][0])
    postorder(tree[target][1])
    sys.stdout.write(target)

preorder('A')
print()
inorder('A')
print()
postorder('A')