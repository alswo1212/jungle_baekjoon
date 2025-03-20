import sys
input = sys.stdin.readline
row_check = [0]*9
col_check = [0]*9
area_check = [0]*9
points = []

result = []
for i in range(9):
    row = list(map(int, input().rstrip()))
    result.append(row)
    for j in range(9):
        num = row[j]
        if num == 0:
            points.append((i,j))
        else:
            bit = 1 << (num-1)
            row_check[i] |= bit
            col_check[j] |= bit
            area_check[3 * (i//3) + (j//3)] |= bit

def dfs(idx:int) -> bool:
    if idx == len(points):
        return True
    
    row, col = points[idx]
    for num in range(9):
        bit = 1 << num
        if row_check[row] & bit: continue
        if col_check[col] & bit: continue
        if area_check[3*(row//3) + (col//3)] & bit: continue

        row_check[row] |= bit
        col_check[col] |= bit
        area_check[3*(row//3) + (col//3)] |= bit
        result[row][col] = num+1
        
        if dfs(idx+1):
            return True

        row_check[row] ^= bit
        col_check[col] ^= bit
        area_check[3*(row//3) + (col//3)] ^= bit
        result[row][col] = 0
    return False
        
dfs(0)
for r in result:print(''.join(map(str, r)))