from collections import Counter
import re
def solution(s):
    return list(map(lambda x: int(x[0]),Counter(re.findall('\d+', s)).most_common()))