from math import ceil

def time_2_int(time:str):
    h, m = time.split(":")
    return int(h)*60 + int(m)

def convert_code(code:str):
    code_map = {'C':'0','D':'1','F':'2','G':'3','A':'4',}
    result = ''
    for c in code:
        if c == '#':
            result = result[:-1] + code_map[result[-1]]
        else:
            result += c
    
    return result
        
def solution(m, musicinfos):
    candidate = []
    m = convert_code(m)
    for i, musicinfo in enumerate(musicinfos):
        st, et, name, code = musicinfo.split(',')
        code = convert_code(code)
        music_len = time_2_int(et) - time_2_int(st)
        full_code = code * ceil(music_len / len(code))
        
        if m in full_code[:music_len]:
            candidate.append([name, music_len, i])
    candidate.sort(key=lambda ar: -ar[1])
    
    return candidate[0][0] if candidate else "(None)"