from itertools import permutations
from collections import deque

def str_2_list(expression:str):
    answer = []
    idx = 0
    for i, c in enumerate(expression):
        if not c.isnumeric():
            answer.append(int(expression[idx:i]))
            answer.append(c)
            idx = i+1
    answer.append(int(expression[idx:]))
    return answer

def calc(exp_list:list[int], order: list[str]):
    q1 = deque(exp_list)
    q2 = deque()
    for o in order:
        target_q = q1 if q1 else q2
        other_q =  q2 if q1 else q1
        while target_q:
            word = target_q.popleft()
            if o == word:
                if o == '*':
                    other_q.append(other_q.pop() * target_q.popleft())
                elif o == '+':
                    other_q.append(other_q.pop() + target_q.popleft())
                else:
                    other_q.append(other_q.pop() - target_q.popleft())
            else:
                other_q.append(word)
    
    return  abs(q1[0] if q1 else q2[0])

def solution(expression:str):
    exp_list = str_2_list(expression)
    return max(calc(exp_list, order) for order in permutations("+-*", 3))