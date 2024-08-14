import sys
import itertools

while True:
    inputs = list(map(int, sys.stdin.readline().split()))
    length = inputs[0]
    if length == 0: break

    nums = inputs[1:]
    combi = list(itertools.combinations(nums, 6))
    for comb in combi:
        print(*comb)

    print()