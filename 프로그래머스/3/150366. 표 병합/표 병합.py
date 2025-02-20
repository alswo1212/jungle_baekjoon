def solution(commands):
    answer = []
    EMPTY = 'EMPTY'
    groups = [[{(i, j)} for j in range(50)] for i in range(50)]
    p_2_value = [[EMPTY] * 50 for _ in range(50)]

    for command in commands:
        cs = command.split(' ')
        if cs[0] == 'UPDATE':
            if len(cs) >= 4:
                r, c = int(cs[1]) - 1, int(cs[2]) - 1
                for p in groups[r][c]:
                    p_2_value[p[0]][p[1]] = cs[3]
            else:
                for i in range(50):
                    for j in range(50):
                        if p_2_value[i][j] == cs[1]:
                            p_2_value[i][j] = cs[2]

        elif cs[0] == 'MERGE':
            r1, c1, r2, c2 = map(lambda c: int(c) - 1, cs[1:])
            if groups[r1][c1] == groups[r2][c2]:
                continue
            
            val1, val2 = p_2_value[r1][c1], p_2_value[r2][c2]
            new_group = groups[r1][c1] | groups[r2][c2]
            new_val = val1 if val1 != EMPTY else val2

            for p in new_group:
                groups[p[0]][p[1]] = new_group
                p_2_value[p[0]][p[1]] = new_val

        elif cs[0] == 'UNMERGE':
            r, c = map(lambda c: int(c) - 1, cs[1:])
            val = p_2_value[r][c]
            target = groups[r][c]

            for i, j in target:
                groups[i][j] = {(i, j)}
                p_2_value[i][j] = EMPTY

            p_2_value[r][c] = val

        elif cs[0] == 'PRINT':
            r, c = map(lambda c: int(c) - 1, cs[1:])
            answer.append(p_2_value[r][c])

    return answer