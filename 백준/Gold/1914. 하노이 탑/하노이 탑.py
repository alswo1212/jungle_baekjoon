n = int(input())

print(2 ** n - 1)
if n <= 20 :
    def hanoi(floor:int, start:int, end:int):
        mid = 6 - start - end

        if floor > 1 : hanoi(floor-1, start, mid)
        
        print(start, end)

        if floor > 1 : hanoi(floor-1, mid, end)

    hanoi(n, 1, 3)