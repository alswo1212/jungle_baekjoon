from collections import deque
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        direc = deque([
            {'x':1, 'y':0}, # 우
            {'x':0, 'y':1}, # 하
            {'x':-1, 'y':0}, # 좌
            {'x':0, 'y':-1}, # 상
            ])
        point = {'x':0, 'y':0}
        cnt = 1
        for _ in range(n * n):
            matrix[point['y']][point['x']] = cnt
            cnt += 1
            if not (
                0 <= point['x'] + direc[0]['x'] < n and 
                0 <= point['y'] + direc[0]['y'] < n and
                matrix[point['y'] + direc[0]['y']][point['x'] + direc[0]['x']] == 0
            ):
                direc.append(direc.popleft())
            point['x'] += direc[0]['x']
            point['y'] += direc[0]['y']
        
        return matrix