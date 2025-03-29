def solution(m, musicinfos):
    answer = ''
    note_index = {
        'C#':'c','D#':'d','F#':'f', 'G#':'g','A#':'a','B#':"b"
    }
    
    def time_2_int(time:str)->int:
        return 60*int(time[:2]) + int(time[3:])
    
    def parse_music(music:str)->str:
        for key, val in note_index.items():
            music = music.replace(key, val)
        return music
    
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