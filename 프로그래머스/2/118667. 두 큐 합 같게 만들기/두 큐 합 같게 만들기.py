from collections import deque
def solution(queue1:list[int], queue2:list[int]):
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    limit = (len(queue1) + len(queue2)) * 2
    count = 0
    for _ in range(limit):
        if q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
            count += 1
        elif q1_sum < q2_sum:
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num
            count += 1
        else:
            return count
            
    return -1