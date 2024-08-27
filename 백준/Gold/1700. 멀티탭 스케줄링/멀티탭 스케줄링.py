from sys import maxsize
N, M = map(int, input().split())
arr = list(map(int, input().split()))

tab = set()
result = 0
for i, num in enumerate(arr):
    tab.add(num)
    if len(tab) > N:
        remove_idx = -1
        remove_val = 0
        for tab_num in tab:
            try:
                idx = arr[i:].index(tab_num)
            except:
                idx = M
            if remove_idx < idx:
                remove_idx = idx
                remove_val = tab_num

        tab.discard(remove_val)
        result += 1

print(result)