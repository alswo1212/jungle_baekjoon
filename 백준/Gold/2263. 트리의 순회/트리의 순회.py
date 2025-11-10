import sys
input = sys.stdin.readline

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []
stack = [[0,N,0,N]]
inorder_idxs = [0]*(N+1)

for i, num in enumerate(inorder):
    inorder_idxs[num] = i

while stack:
    in_start, in_end, post_start, post_end = stack.pop()
    if in_start >= in_end:
        continue
    target = postorder[post_end-1]
    preorder.append(target)
    i = inorder_idxs[target]
    length = i - in_start
    stack.append([i+1, in_end, post_start+length, post_end-1])
    stack.append([in_start, i, post_start, post_start+length])

print(*preorder)