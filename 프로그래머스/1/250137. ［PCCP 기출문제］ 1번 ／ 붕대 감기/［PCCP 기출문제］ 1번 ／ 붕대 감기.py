def solution(bandage, health, attacks):
    answer = health
    t, x, y = bandage
    now = 0
    for time, damage in attacks:
        iterval = (time - now - 1)
        answer = min(health, answer + x*iterval + iterval // t * y)
        answer -= damage
        now = time
        if answer <= 0:
            return -1

    return answer