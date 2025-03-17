from collections import deque
def solution(queue1, queue2):
    answer = 0
    is_find = False
    q1, q1_sum = deque(queue1), sum(queue1)
    q2, q2_sum = deque(queue2), sum(queue2)
    for _ in range((len(queue1)+len(queue2) << 1)):
        if q1_sum == q2_sum:
            is_find = True
            break
        
        if q1_sum > q2_sum:
            num = q1.popleft()
            q1_sum -= num
            q2_sum += num
            q2.append(num)
        else:
            num = q2.popleft()
            q2_sum -= num
            q1_sum += num
            q1.append(num)
        answer += 1
            
    return answer if is_find else -1