import sys
sys.setrecursionlimit(int(1e8))
inputs = [int(line) for line in sys.stdin.readlines()]
tree = {}

def add_tree(tree, num):
    while True:
        if tree['key'] >= num:
            if tree['l'] == 0:
                tree['l'] = {'key':num, 'l': 0, 'r':0}
                break
            else:
                tree = tree['l']
        else :
            if tree['r'] == 0:
                tree['r'] = {'key':num, 'l': 0, 'r':0}
                break
            else:
                tree = tree['r']

for num in inputs:
    if 'key' not in tree:
        tree = {'key':num, 'l': 0, 'r':0}
        continue
    add_tree(tree, num)

def print_tree_postorder(tree):
    if tree['l'] != 0:
        print_tree_postorder(tree['l'])
    if tree['r'] != 0:
        print_tree_postorder(tree['r'])
    sys.stdout.write(f'{tree["key"]}\n')

print_tree_postorder(tree)