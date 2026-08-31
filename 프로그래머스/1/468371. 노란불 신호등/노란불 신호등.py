from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    cycles = [g+y+r for g,y,r in signals]
    limit = reduce(lcm, cycles)

    for t in range(1, limit+1):
        ok = True

        for g, y, r in signals:
            cycle = g + y + r
            mod = t % cycle

            if not (g <= mod <= g+y-1):
                ok = False
                break

        if ok:
            return t+1

    return -1