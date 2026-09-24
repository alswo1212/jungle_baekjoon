def solution(p:str):
    if not p: return p

    counts = [0, 0]
    u, v = '', ''

    for i, c in enumerate(p):
        counts[0 if c == '(' else 1] += 1
        if counts[0] == counts[1]:
            u, v = p[:i+1], p[i+1:]
            break

    if u[0] == '(':
        return u + solution(v)

    return f'({solution(v)}){''.join('(' if c == ')' else ')' for c in u[1:-1])}'