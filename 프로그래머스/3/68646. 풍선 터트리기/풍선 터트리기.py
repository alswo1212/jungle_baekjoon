def solution(a):
    answer = 0
    left, right = float('inf'), float('inf')
    min_map = [[0, 0] for _ in range(len(a))]

    # 왼쪽 범위에서 최솟값 찾기
    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
        min_map[i][0] = left

    # 오른쪽 범위에서 최솟값 찾기
    for i in range(len(a) - 1, -1, -1):
        if right > a[i]:
            right = a[i]
        min_map[i][1] = right

    # 찾은 최솟값 데이터를 가지고 기준 숫자의 양쪽이 모두 기준 숫자보다 작으면 answer += 1
    for i in range(len(a)):
        if a[i] <= min_map[i][0] or a[i] <= min_map[i][1]:
            answer += 1

    return answer