def solution(m, musicinfos):
    answer = ''
    note_index = {
        'C#':'b','D#':'d','F#':'g', 'G#':'i','A#':'k','B#':'m','E#':'n',
        'C':'a','D':'c','E':'e','F':'f','G':'h','A':'j','B':'l'
    }
    
    def time_2_int(time:str)->int:
        return 60*int(time[:2]) + int(time[3:])
    
    def parse_music(music:str)->str:
        result = ''
        i = 0
        while i < len(music):
            if i + 1 < len(music) and music[i+1] == '#':
                result += note_index[music[i:i+2]]
                i += 2
                continue
            result += note_index[music[i]]
            i += 1
        return result
    
    m = parse_music(m)
    max_play_time = 0
    for info in musicinfos:
        start_time, end_time, title, music = info.split(',')
        play_time = time_2_int(end_time) - time_2_int(start_time)
        music = parse_music(music)
        if play_time > len(music):
            music *= play_time // len(music) + 1
        if m in music[:play_time] and max_play_time < play_time:
            answer = title
            max_play_time = play_time
    
    if max_play_time == 0:
        return "(None)"
    
    return answer