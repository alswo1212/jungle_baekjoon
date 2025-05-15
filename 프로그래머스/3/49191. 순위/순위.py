from collections import defaultdict, deque
def solution(n, results):
    def get_cnt(start:int, edges:defaultdict)->int:
        q = deque([start])
        marks = set()
        while q:
            now = q.popleft()
            for node in edges[now]:
                if node in marks: continue
                q.append(node)
                marks.add(node)
        return len(marks)
    
    answer = 0
    wins = defaultdict(list)
    loses = defaultdict(list)
    for w, l in results:
        wins[l].append(w)
        loses[w].append(l)

    for now in range(1, n+1):
        if get_cnt(now, wins) + get_cnt(now, loses) == n-1:
            answer += 1
    return answer