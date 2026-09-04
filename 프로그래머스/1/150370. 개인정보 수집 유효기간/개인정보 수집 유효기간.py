def solution(today, terms, privacies):
    def to_int(date:str):
        year, month, day = map(int, date.split('.'))
        return year * 12 * 28 + month * 28 + day
    
    answer = []
    target = to_int(today)
    term_dict = {}
    for term in terms:
        type, month = term.split(' ')
        term_dict[type] = int(month) * 28

    for i, privacy in enumerate(privacies):
        sign_in, type = privacy.split(' ')
        if to_int(sign_in) + term_dict[type] <= target:
            answer.append(i+1)
    return answer