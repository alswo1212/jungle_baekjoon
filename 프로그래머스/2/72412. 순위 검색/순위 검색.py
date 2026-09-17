from bisect import bisect_left
from collections import defaultdict
from itertools import product

def solution(info, query):
    score_table = defaultdict(list)

    for entry in info:
        language, job, career, food, score = entry.split()
        score = int(score)

        for key in product(*[(value, "-") for value in (language, job, career, food)]):
            score_table[key].append(score)

    for scores in score_table.values():
        scores.sort()

    answer = []
    for q in query:
        tokens = q.split()
        language, job, career, food = tokens[0], tokens[2], tokens[4], tokens[6]
        target_score = int(tokens[7])

        scores = score_table[(language, job, career, food)]
        answer.append(len(scores) - bisect_left(scores, target_score))

    return answer