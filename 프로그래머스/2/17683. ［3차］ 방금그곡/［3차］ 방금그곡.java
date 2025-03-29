import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public String solution(String m, String[] musicinfos) {
        Map<String, String> map = Map.of("C#","c","D#","d","F#","f","G#","g","A#","a","B#","b");
        PriorityQueue<Song> pq = new PriorityQueue<>((s1, s2) -> Integer.compare(s2.playTime, s1.playTime));
        String temp = m;

        for (String key : map.keySet()) {
            temp = temp.replace(key, map.get(key));
        }

        for (String info : musicinfos) {
            pq.add(new Song(info, map));
        }

        while (!pq.isEmpty()) {
            Song song = pq.poll();

            if(song.notes.contains(temp)){
                return song.songName;
            }
            
        }
        return "(None)";
    }
}

class Song{
    int startTime;
    int endTime;
    int playTime;
    String songName;
    String notes;

    private Song() {;}

    public Song(String info, Map<String, String> map) {
        String[] infos = info.split(",");
        this.startTime = parseTime(infos[0]);
        this.endTime = parseTime(infos[1]);
        this.playTime = this.endTime - this.startTime;
        this.songName = infos[2];


        for (String key : map.keySet()) {
            infos[3] = infos[3].replace(key, map.get(key));
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < this.playTime; i++){
            sb.append(infos[3].charAt(i % infos[3].length()));
        }
        this.notes = sb.toString();
    }
    
    private int parseTime(String time){
        String[] times = time.split(":");
        return Integer.parseInt(times[0]) * 60 + Integer.parseInt(times[1]);
    }
}