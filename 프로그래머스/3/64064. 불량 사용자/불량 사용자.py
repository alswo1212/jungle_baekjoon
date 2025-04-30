def solution(user_id, banned_id):
    def split_id(id:str)->list:
        result = []
        before = id[0]
        idx = 0
        for i in range(len(id)):
            c = id[i]
            if (before == '*' and c != '*') or (before != '*' and c == '*'):
                result.append(id[idx:i])
                idx = i
                before = c

        if idx < len(id):
            result.append(id[idx:])

        return result
    
    def check_ban(id:str, query:list, check_len:int):
        if len(id) != check_len:
            return False
        i = 0
        for q in query:
            if q[0] != '*' and not id[i:].startswith(q):
                return False
            i += len(q)
            if i > len(id):
                return False
        return i == check_len
    
    def dfs(ban_idx:int, bits:int):
        nonlocal result
        if ban_idx == len(banned_list):
            result.add(bits)
            return
        
        for i in range(n):
            bit = 1 << i
            if bits & bit:
                continue

            if check_ban(user_id[i], banned_list[ban_idx], len(banned_id[ban_idx])):
                dfs(ban_idx+1, bit | bits)
            
    n = len(user_id)
    banned_list = [split_id(b_id) for b_id in banned_id]
    result = set()
    dfs(0, 0)
    
    return len(result)