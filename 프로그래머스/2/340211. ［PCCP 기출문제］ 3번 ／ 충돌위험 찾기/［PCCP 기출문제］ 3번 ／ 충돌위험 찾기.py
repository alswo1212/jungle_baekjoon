from collections import deque, defaultdict
def solution(points, routes):
    def check_bump(q:list) -> int:
        answer = 0
        point_then_cnt = defaultdict(int)
        for p1, _ in q:
            point_then_cnt[p1] += 1
        
        for v in point_then_cnt.values():
            if v > 1:
                answer += 1
        return answer

    q = deque()
    for i in range(len(routes)):
        route = routes[i]
        start = points[route[0]-1]
        q.append([(start[0], start[1]), deque(route)])
    answer = 0
        
    while q:
        temp_list = []
        while q:
            temp_list.append(q.popleft())
        answer += check_bump(temp_list)
        for i  in range(len(temp_list)):
            now, route = temp_list[i]
            if (now[0] == points[route[0]-1][0]
                and
                now[1] == points[route[0]-1][1]):
                route.popleft()
            
            if len(route) == 0:
                continue

            next = points[route[0]-1]
            if now[0] < next[0]:
                now = (now[0]+1, now[1])
            elif now[0] > next[0]:
                now = (now[0]-1, now[1])
            elif now[1] < next[1]:
                now = (now[0], now[1]+1)
            else:
                now = (now[0], now[1]-1)
            q.append([now, route])

    return answer