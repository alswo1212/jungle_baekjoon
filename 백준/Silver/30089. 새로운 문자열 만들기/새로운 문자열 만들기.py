from collections import deque
T = int(input())
def make_str(S:str, q:deque, idx:int):
    temp = S + "".join(q)
    length = len(temp)
    flag = True
    for i in range(0, length // 2 + 1):
        if temp[i] != temp[length-i-1]:
            flag = False
            break

    q.appendleft(S[idx])
    return temp if flag else make_str(S, q, idx+1)
q = deque()
for _ in range(T):
    S = input().strip()
    print(make_str(S, q, 0))
    q.clear()