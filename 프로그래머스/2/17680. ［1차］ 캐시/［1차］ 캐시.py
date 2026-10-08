from collections import OrderedDict

def solution(cacheSize, cities):
    if cacheSize == 0 : return len(cities) * 5
    answer = 0
    cache = OrderedDict()
    for city in cities:
        target = city.upper()
        if target in cache:
            cache.pop(target)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.popitem(last=False)
            answer += 5
        cache[target] = answer
    return answer