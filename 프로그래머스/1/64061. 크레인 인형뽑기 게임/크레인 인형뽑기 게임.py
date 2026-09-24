def solution(board:list[list[int]], moves:list[int]):
    answer = 0
    N = len(board)
    bag = []
    lines = [[] for _ in range(N)]
    for j in range(N):
        i = N-1
        while i >= 0 and board[i][j]: 
            lines[j].append(board[i][j])
            i -= 1

    for num in moves:
        idx = num - 1
        if lines[idx]:
            bag.append(lines[idx].pop())
        if len(bag) >= 2 and bag[-1] == bag[-2]:
            bag.pop()
            bag.pop()
            answer += 2

    return answer