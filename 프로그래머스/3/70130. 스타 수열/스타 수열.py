def solution(a):
    def get_star_len(arr:list,idxs:list)->int:
        used = set()
        n = len(arr)-1
        for idx in idxs:
            if idx in used:
                continue
            if idx != 0 and idx-1 not in used and arr[idx-1] != arr[idx]:
                used.add(idx)
                used.add(idx-1)
            elif idx != n and idx+1 not in used and arr[idx] != arr[idx+1]:
                used.add(idx)
                used.add(idx+1)
                
        return len(used)
    
    answer = -1
    lists = {}
    for i, num in enumerate(a):
        if num not in lists:
            lists[num] = []
        lists[num].append(i)

    for arr in lists.values():
        temp = get_star_len(a, arr)
        if temp > answer:
            answer = temp

    return answer