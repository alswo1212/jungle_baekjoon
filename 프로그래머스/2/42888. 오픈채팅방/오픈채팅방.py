from collections import defaultdict
def solution(record):
    answer = []
    nicks = defaultdict(str)
    for r in record:
        inputs = r.split()
        if inputs[0] == 'Enter':
            answer.append((inputs[1],'님이 들어왔습니다.'))
            nicks[inputs[1]] = inputs[2]
        elif inputs[0] == 'Leave':
            answer.append((inputs[1],'님이 나갔습니다.'))
        elif inputs[0] == 'Change':
            nicks[inputs[1]] = inputs[2]

    for i in range(len(answer)):
        uid = answer[i][0]
        answer[i] = nicks[uid] + answer[i][1]
            
    return answer