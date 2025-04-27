from collections import defaultdict
def solution(genres, plays):
    answer = []
    cnts = defaultdict(int)
    gens = defaultdict(list)
    for i in range(len(genres)):
        genre = genres[i]
        gens[genre].append((plays[i], i))
        cnts[genre] += plays[i]
    sorted_genre = sorted(cnts.items(), key=lambda item: item[1], reverse=True)

    for genre, cnt in sorted_genre:
        gens[genre].sort(key=lambda it: (-it[0], it[1]))
        answer.extend(map(lambda it: it[1],gens[genre][:2]))
    return answer