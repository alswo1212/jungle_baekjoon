def solution(n, info):
    max_diff = 0           # 현재까지 발견한 최대 점수 차
    best_candidate = None  # 조건에 맞는 라이언의 화살 배분 배열

    # 0 ~ 2^11 - 1 까지 모든 비트마스크 탐색 (각 비트는 해당 점수를 가져가기 위한 선택 여부)
    for mask in range(1 << 11):
        ryan = [0] * 11  # 10점부터 0점까지 라이언의 배분
        arrows_used = 0  # 사용한 화살 수

        # 각 점수에 대해, 해당 비트가 켜져있다면 어피치보다 1발 더 맞혀 승리해야 함
        for i in range(11):
            if mask & (1 << i):
                required = info[i] + 1
                ryan[i] = required
                arrows_used += required

        # 만약 사용한 화살 수가 n보다 초과하면 불가능한 배분이므로 넘어감
        if arrows_used > n:
            continue

        # 남은 화살은 0점(배열의 마지막 인덱스, 즉 index 10)에 모두 할당
        ryan[10] += n - arrows_used

        # 두 선수의 점수 계산 (각 i번째 원: 점수 = 10 - i)
        ryan_score, apeach_score = 0, 0
        for i in range(11):
            # 두 선수 모두 해당 점수에 화살을 맞히지 않았다면 무시
            if info[i] == 0 and ryan[i] == 0:
                continue
            # 라이언이 더 많이 맞혔다면 라이언이 해당 점수를 획득, 그렇지 않으면 어피치가 획득
            if ryan[i] > info[i]:
                ryan_score += (10 - i)
            else:
                apeach_score += (10 - i)

        diff = ryan_score - apeach_score
        # 라이언이 이기지 못하면 패스
        if diff <= 0:
            continue

        # 더 큰 점수 차를 발견하면 후보 갱신
        if diff > max_diff:
            max_diff = diff
            best_candidate = ryan
        # 점수 차가 같다면, 낮은 점수를 더 많이 맞힌 경우(배열의 뒤쪽 원소가 큰 경우)를 선택
        elif diff == max_diff:
            # 배열을 뒤집어 비교하면 낮은 점수부터 비교하는 효과가 있음
            if ryan[::-1] > best_candidate[::-1]:
                best_candidate = ryan

    return best_candidate if best_candidate is not None else [-1]