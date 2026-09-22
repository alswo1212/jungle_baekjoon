def solution(s:str):
    answer = []
    arr = s.removeprefix("{{").removesuffix("}}").split('},{')
    arr.sort(key=lambda ar: len(ar))
    already = set()
    for ss in arr:
        sub_arr = list(map(int, ss.split(',')))
        for num in sub_arr:
            if num not in already:
                answer.append(num)
                already.add(num)
                break
    return answer