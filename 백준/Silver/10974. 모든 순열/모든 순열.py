n = int(input())
def permute(n, depth, arr, bits):
    if n == depth:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if (1 << i) & bits : continue
        
        permute(n, depth+1, [*arr, i], bits | (1 << i))
permute(n, 0, [], 0)