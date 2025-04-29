def solution(gems):
    answer = [1, len(gems)]
    left, right = 0, 0
    cnts = {}
    gems_cnt = len(set(gems))

    while left < len(gems):
        if len(cnts) == gems_cnt:
            if answer[1] - answer[0] > right - left - 1:
                answer[0], answer[1] = left+1, right
            cnts[gems[left]] -= 1
            if cnts[gems[left]] == 0:
                cnts.pop(gems[left])
            left += 1
        else:
            if right < len(gems):
                if gems[right] not in cnts:
                    cnts[gems[right]] = 0
                cnts[gems[right]] += 1
                right += 1
            else:
                cnts[gems[left]] -= 1
                if cnts[gems[left]] == 0:
                    cnts.pop(gems[left])
                left += 1
                
    return answer