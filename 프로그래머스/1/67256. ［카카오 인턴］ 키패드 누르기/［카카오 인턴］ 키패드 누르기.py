def get_dist(p1:int, p2:int):
    p1, p2 = p1-1, p2-1
    row = abs(p1 // 3 - p2 // 3)
    col = abs(p1 % 3 - p2 % 3)
    return row + col

def solution(numbers:list[int], hand:str):
    answer = ''
    lr_hands = [10, 12]
    for number in numbers:
        if number == 0: number = 11
        modul = number % 3
        if modul != 2:
            answer += 'L' if modul == 1 else 'R'
            lr_hands[0 if modul == 1 else 1] = number
        else:
            l_dist = get_dist(lr_hands[0], number)
            r_dist = get_dist(lr_hands[1], number)
            if l_dist == r_dist:
                answer += 'L' if hand == 'left' else 'R'
                lr_hands[0 if hand == 'left' else 1] = number
            else:
                answer += 'L' if l_dist < r_dist else 'R'
                lr_hands[0 if l_dist < r_dist else 1] = number
                
    return answer