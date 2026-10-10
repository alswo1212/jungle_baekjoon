from collections import Counter
def solution(str1, str2):
    masic_num = 65536
    str1, str2 = str1.upper(), str2.upper()
    if str1 == str2: return masic_num
    zips1 = Counter([str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    zips2 = Counter([str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()])
    if len(zips1) == len(zips2) == 0: 
        return 0
    
    min_zip = sum(min(zips1[key], zips2[key]) for key in zips1.keys() if key in zips2)
    all_keys = set([*zips1.keys(), *zips2.keys()])
    max_zip = sum(max(zips1[key], zips2[key]) for key in all_keys)
        
    return min_zip / max_zip * masic_num // 1