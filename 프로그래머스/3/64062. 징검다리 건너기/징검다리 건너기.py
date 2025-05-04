def solution(stones, k):
    answer = float('inf')
    stones.append(float('inf'))
    stack = [(-1, float('inf'))]
    for i, stone in enumerate(stones):
        node = (i, stone)
        temp = 0
        while stack[-1][1] < node[1]:
            poped = stack.pop()
            if i - poped[0] <= k:
                temp = max(poped[1], temp)

        if i - stack[-1][0] > k and answer > temp:
            answer = temp
        
        stack.append(node)
        
    return answer