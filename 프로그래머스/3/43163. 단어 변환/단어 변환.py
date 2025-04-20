from collections import deque
def solution(begin, target, words):
    def cnt_diff(word1:str, word2:str)->int:
        return sum(1 for i in range(len(word1)) if word1[i] != word2[i])
            
    m = len(words)
    nexts = set(i for i in range(m))
    q = deque([(begin, nexts, 0)])
    while q:
        word, candi, cnt = q.popleft()
        if word == target:
            return cnt
        
        for idx in candi:
            next_word = words[idx]
            if 1 == cnt_diff(word, next_word):
                q.append((next_word, candi.difference({idx}), cnt+1))

    return 0