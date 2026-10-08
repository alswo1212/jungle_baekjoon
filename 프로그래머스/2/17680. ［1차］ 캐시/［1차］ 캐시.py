def solution(cacheSize, cities):
    answer = 0
    cache = {}
    for city in cities:
        target = city.upper()
        if target in cache:
            cache[target] = answer
            answer += 1
        else:
            if cacheSize and len(cache) == cacheSize:
                oldest = ['', float('inf')]
                for key, value in cache.items():
                    if oldest[1] > value:
                        oldest[0], oldest[1] = key, value
                cache.pop(oldest[0])
            
            if cacheSize:
                cache[target] = answer
            answer += 5
    return answer