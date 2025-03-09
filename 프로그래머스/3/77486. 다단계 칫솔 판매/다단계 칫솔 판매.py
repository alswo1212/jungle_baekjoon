from collections import defaultdict
def solution(enroll, referral, seller, amount):
    ref = {}
    for i in range(len(referral)): ref[enroll[i]] = referral[i]

    incomes = defaultdict(int)
    for i in range(len(seller)): 
        money = amount[i]*100
        now_seller = seller[i]
        while money and now_seller != '-':
            incomes[now_seller] += money - (money // 10)
            money //= 10
            now_seller = ref[now_seller]
        
    return list(map(lambda name: incomes[name], enroll))