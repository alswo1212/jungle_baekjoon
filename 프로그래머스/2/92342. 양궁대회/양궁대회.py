def solution(n, info):
    answer = [-1]
    # 봐야할 인덱스, 남은 화살 수, 현재까지 배열, 어피치 점수, 라이언 점수
    stack = [(0, n, [0]*11, 0, 0)]
    max_diff = 0
    while stack:
        idx, arrow_cnt, arr, apeach, lion = stack.pop()
        if idx == 11:
            arr[-1] = arrow_cnt
            diff = lion - apeach
            if diff > max_diff:
                max_diff = diff
                answer = arr
            elif diff == max_diff and diff != 0:
                for i in range(10, -1, -1):
                    if arr[i] != answer[i]:
                        if arr[i] > answer[i]:
                            answer = arr
                        break
            continue
        
        if info[idx] > 0:
            stack.append((idx+1, arrow_cnt, [*arr], apeach+(10-idx), lion))
        else:
            stack.append((idx+1, arrow_cnt, [*arr], apeach, lion))

        for i in range(info[idx]+1, arrow_cnt + 1):
            copy = [*arr]
            copy[idx] = i
            stack.append((idx+1, arrow_cnt-i, copy, apeach, lion+(10-idx)))

    return answer