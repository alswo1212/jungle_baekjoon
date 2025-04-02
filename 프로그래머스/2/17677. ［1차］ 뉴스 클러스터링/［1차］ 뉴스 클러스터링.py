import re
from collections import Counter
def solution(str1, str2):
    def J(A:set,B:set)->float:
        hap = len(A|B)
        if hap == 0:
            return 1
        return len(A & B) / len(A | B)
    
    str1, str2 = str1.lower(), str2.lower()
    count1 = Counter(str1[i:i+2] for i in range(len(str1)-1) if len(re.findall('[a-z]', str1[i:i+2])) == 2)
    count2 = Counter(str2[i:i+2] for i in range(len(str2)-1) if len(re.findall('[a-z]', str2[i:i+2])) == 2)
    set1 = set((k, i) for k, v in count1.items() for i in range(v) )
    set2 = set((k, i) for k, v in count2.items() for i in range(v) )
    
    return int(J(set1, set2) * 65536)