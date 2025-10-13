from functools import cache
import sys

lines = sys.stdin.readlines()
@cache
def getKantore(n:int) -> str:
    if n == 0:
        return '-'
    
    temp = getKantore(n-1)
    return temp + (' ' * len(temp)) + temp

for line in lines:
    print(getKantore(int(line)))