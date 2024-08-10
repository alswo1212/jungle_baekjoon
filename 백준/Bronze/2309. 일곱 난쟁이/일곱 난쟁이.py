dwarfs = [int(input()) for _ in range(9)]

is_find = False
finded = []
visit = [False] * 9

def make_finded(dwarfs, ):
    global is_find
    if is_find : return
    if len(finded) == 7:
        if sum(finded) == 100:
            is_find = True
            finded.sort()
            for dwarf in finded : print(dwarf)
        return
    
    for i in range(9):
        if visit[i] : continue

        visit[i] = True
        finded.append(dwarfs[i])
        make_finded(dwarfs)
        finded.pop()
        visit[i] = False

make_finded(dwarfs)