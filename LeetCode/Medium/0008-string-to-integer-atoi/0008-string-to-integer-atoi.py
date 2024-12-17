class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: 
            return 0
        def is_oper(c:str):
           return ord(c) == 43 or ord(c) == 45
        
        idx = 0
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        result = []
        min_val = (2 << 30) * -1
        max_val = (2 << 30) - 1
        if idx < len(s) and is_oper(s[idx]):
            result.append(s[idx])
            idx += 1
        
        while idx < len(s):
            if 48 > ord(s[idx]) or ord(s[idx]) > 57:
                break
            result.append(s[idx])
            idx += 1

        if len(result) == 1 and is_oper(result[0]):
            return 0
        elif len(result) == 0:
            return 0
        else :
            result = int(''.join(result))
            if result < min_val:
                return min_val
            elif result > max_val:
                return max_val
            return result