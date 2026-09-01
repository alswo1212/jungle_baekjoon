from collections import deque, defaultdict

def overlap(arr1:list[int], arr2:list[int]): return arr1[0] < arr2[1] and arr1[1] >= arr2[0]

def solution(message:str, spoiler_ranges:list[list[int]]):
    answer = 0
    word_ranges = []
    words = message.split(' ')
    word_counts = defaultdict(int)
    spoiler_q = deque(spoiler_ranges)
    
    word_i = 0
    spo_i = 0
    for word in words:
        word_range = [word_i, word_i + len(word)]
        word_ranges.append(word_range)
        while len(spoiler_ranges) > spo_i and spoiler_ranges[spo_i][1] < word_i:
            spo_i += 1
        
        if spo_i < len(spoiler_ranges) and not overlap(spoiler_ranges[spo_i], word_range):
            word_counts[word] += 1
        elif spo_i >= len(spoiler_ranges):
            word_counts[word] += 1

        word_i += len(word) + 1
    
    for word_i, word in enumerate(words):
        word_range = word_ranges[word_i]
        while spoiler_q and spoiler_q[0][1] < word_range[0]:
            spoiler_q.popleft()
        
        if spoiler_q and overlap(spoiler_q[0], word_range) and word_counts[word] < 1:
            answer += 1
            word_counts[word] += 1
    
    return answer