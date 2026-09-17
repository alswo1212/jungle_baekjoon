from bisect import bisect_left
def make_all_cases():
    options = [
        ["cpp", "java", "python", "-"],
        ["backend", "frontend", "-"],
        ["junior", "senior", "-"],
        ["chicken", "pizza", "-"],
    ]
    all_cases = []
    def make_case(idx:int,result:str):
        if idx == len(options):
            all_cases.append(result)
            return
        for word in options[idx]:
            make_case(idx+1, result + word)
    make_case(0, '')
    
    return all_cases
    
def solution(info:list[str], query:list[str]):
    answer = []
    db = { key: [] for key in make_all_cases()}
    
    for selects in info:
        lang, dev, career, food, score = selects.split()
        score = int(score)
        options = [lang, dev, career, food]
        for bits in range(1 << len(options)):
            db_key = ''
            for i in range(len(options)):
                db_key += options[i] if bits % 2 else '-'
                bits >>= 1
            db[db_key].append(score)
            
    for values in db.values(): values.sort()
    
    for q in query:
        lang, _, dev, _, career, _, food, score = q.split()
        score = int(score)
        db_key = lang + dev + career + food
        idx = bisect_left(db[db_key], score)
        answer.append(len(db[db_key]) - idx)
        
    return answer