def solution(users, emoticons):
    answer = [0,0]
    n, m = len(users), len(emoticons)
    lates = [0.9, 0.8, 0.7, 0.6]
    costs = [[e * l for e in emoticons] for l in lates]
    
    for c in range(1 << (m*2)):
        temp = []
        for _ in range(m):
            temp.append(c % 4)
            c >>= 2

        join_cnt = 0
        total_sale = 0
        for late, price in users:
            sale = 0
            for i in range(m):
                if (temp[i]+1)*10 >= late:
                    sale += costs[temp[i]][i]
                if sale >= price:
                    join_cnt += 1
                    sale = 0
                    break
            total_sale += sale

        if answer[0] < join_cnt:
            answer[0], answer[1] = join_cnt, total_sale
        elif answer[0] == join_cnt and answer[1] < total_sale:
            answer[1] = total_sale
    
    return answer