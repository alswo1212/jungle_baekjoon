def solution(s):
    answer = []
    added = set()
    arrs = []
    for temp in s[2:-2].split('},{'):
        arrs.append(list(map(int, temp.split(','))))
    arrs.sort(key=lambda ar: len(ar))
    for arr in arrs:
        for num in arr:
            if num in added:
                continue
            added.add(num)
            answer.append(num)
    
    return answer