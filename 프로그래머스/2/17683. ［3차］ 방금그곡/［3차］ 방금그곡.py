def time_2_int(time:str):
    h, m = time.split(':')
    return int(h)*60 + int(m)

def convert_code(code:str):
    code_map = {'C#':'c','D#':'d','F#':'f','A#':'a','G#':'g',}
    for key, value in code_map.items():
        code = code.replace(key, value)
    return code

def solution(m, musicinfos):
    answer = '(None)'
    max_play_len = 0
    m = convert_code(m)
    
    for musicinfo in musicinfos:
        st, et, name, code = musicinfo.split(',')
        code = convert_code(code)
        play_len = time_2_int(et) - time_2_int(st)
        full_code = code * (play_len // len(code) + 1)
        
        if m in full_code[:play_len] and max_play_len < play_len:
            answer = name
            max_play_len = play_len
    
    return answer