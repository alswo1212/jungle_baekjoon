def solution(s:str):
    if len(s) == 1: return 1
    
    def compress(s:str, length:int):
        result = ''
        idx, N = 0, len(s)
        while idx < N:
            cnt, sub_i = 1, idx + length
            word = s[idx: idx+length]
            while sub_i + length <= N and word == s[sub_i:sub_i+length]:
                cnt += 1
                sub_i += length
            
            result += word if cnt == 1 else f'{cnt}{word}'
            idx += length * cnt

        return result
        
    return min(len(compress(s, length)) for length in range(1, len(s) // 2 + 1))