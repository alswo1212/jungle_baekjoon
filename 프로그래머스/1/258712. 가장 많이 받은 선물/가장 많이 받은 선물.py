from collections import defaultdict

gen_edge = lambda : defaultdict(int)

def solution(friends:list[str], gifts:list[str]):
    answer = 0
    give_edges = defaultdict(gen_edge)
    gift_jisoo = defaultdict(int)
    
    for giver in friends:
        give_edges[giver]
        
    for names in gifts:
        giver, receiver = names.split(' ')
        give_edges[giver][receiver] += 1
        gift_jisoo[giver] += 1
        gift_jisoo[receiver] -= 1
        
    for giver in friends:
        count = 0
        for receiver in friends:
            if giver == receiver: continue
            
            if (
                give_edges[giver][receiver] > give_edges[receiver][giver] or
                (
                    give_edges[giver][receiver] == give_edges[receiver][giver] and
                    gift_jisoo[giver] > gift_jisoo[receiver])
                ):
                count += 1

        answer = max(answer, count)
        
    return answer