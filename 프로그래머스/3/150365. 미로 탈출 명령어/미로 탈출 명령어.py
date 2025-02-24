def solution(n, m, x, y, r, c, k):
    move = abs(x-r) + abs(y-c)
    if k < move or (move % 2 != k % 2):
        return "impossible"
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    direc = [[1,0,'d'],[0,-1,'l'],[0,1,'r'],[-1,0,'u']]
    result = ''
    while k > 0:
        for dx, dy, d in direc:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            dist = abs(r-nx) + abs(c-ny)
            if dist > k:
                continue
            k -= 1
            result += d
            x, y = nx, ny
            break
    
    return result