from bisect import bisect_left
def solution(info, query):
    def combis(arr, idx, result, reduce=''):
        if idx == len(arr):
            result.append(reduce)
            return
        
        for word in arr[idx]:
            combis(arr, idx+1, result, reduce+word)
        return result

    tree = {}
    for key in combis([
        ['-', 'cpp', 'java', 'python'],
        ['-', 'backend', 'frontend'],
        ['-', 'junior', 'senior'],
        ['-', 'chicken', 'pizza'],
    ], 0, []):
        tree[key] = []
        
    for i in range(len(info)):
        la, po, le, fo, sc = info[i].split(' ')
        sc = int(sc)
        
        for key in combis([
            ['-', la],['-', po],['-', le],['-', fo]
        ], 0, []):
            tree[key].append(sc)
    
    for key in tree.keys():
        tree[key].sort()
        
    answer = []
    for q in query:
        la,_,po,_,le,_,fo,sc = q.split(' ')
        sc = int(sc)
        key = la+po+le+fo
        idx = bisect_left(tree[key], sc)
        answer.append(len(tree[key]) - idx)

    return answer