def solution(coin, cards):
    def can_pair(target:int, own:set, other:set) -> bool:
        for num in own:
            if target - num in other:
                return True
        return False
    def remove_pair(target:int, own:set, other:set):
        for num in own:
            if target - num in other:
                own.remove(num)
                other.remove(target - num)
                return
    answer = 1
    n = len(cards)
    target = n+1
    my_card = set(cards[:n//3])
    drowed = set()
    for i in range(n//3, n, 2):
        answer += 1
        drowed.add(cards[i])
        if i+1 == n:
            break
        drowed.add(cards[i+1])

        if can_pair(target, my_card, my_card):
            remove_pair(target, my_card, my_card)
        elif coin >= 1 and can_pair(target, my_card, drowed):
            remove_pair(target, my_card, drowed)
            coin -= 1
        elif coin >= 2 and can_pair(target, drowed, drowed):
            remove_pair(target, drowed, drowed)
            coin -= 2
        else:
            answer -= 1
            break

    return answer