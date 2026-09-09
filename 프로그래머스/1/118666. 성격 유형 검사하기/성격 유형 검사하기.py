from collections import defaultdict

def solution(survey:list[str], choices:list[int]):
    answer = ''
    category = ["RT", "CF", "JM", "AN"]
    counter = defaultdict(int)
    
    for i, choice in enumerate(choices):
        if choice == 4:
            continue
        elif choice < 4:
            counter[survey[i][0]] += 4 - choice
        else:
            counter[survey[i][1]] += choice - 4
    
    for cate in category:
        temp, std = '', 0
        for t in cate:
            if counter[t] > std:
                temp, std = t, counter[t]
        if temp == '':
            temp = cate[0]
        answer += temp
    
    return answer