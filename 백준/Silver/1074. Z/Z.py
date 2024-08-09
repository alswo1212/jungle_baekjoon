N, r, c = map(int, input().split())

result = 0

def  div_4_area(row, col, n):
    if n == 0: return
    global result
    rt = 2 ** (n-1)
    area = int(f'{row // rt}{col // rt}', 2)
    
    result += (rt ** 2) * area

    div_4_area(row % rt, col % rt, n - 1)

div_4_area(r, c, N)

print(result)