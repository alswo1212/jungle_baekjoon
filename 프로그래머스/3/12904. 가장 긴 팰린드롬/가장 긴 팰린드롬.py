def solution(s):
    answer, n = 0, len(s)

    def get_palin_len(left:int, right:int)->int:
        nonlocal n
        while 0 <= left < n and 0 <= right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        answer = max(answer, get_palin_len(i, i), get_palin_len(i, i+1))

    return answer