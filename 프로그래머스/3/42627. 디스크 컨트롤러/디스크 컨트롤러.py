from heapq import heappush, heappop
def solution(jobs):
    answer = 0
    # (need_time, request_at, idx)
    tasks = [(job[1], job[0], i) for i, job in enumerate(jobs)]
    tasks.sort(key=lambda it: it[1])
    now = 0
    q = []

    for task in tasks:
        if not q or now >= task[1]:
            if not q:
                now = task[1]
            heappush(q, task)
            continue
        
        while q and now <= task[1]:
            cur_task = heappop(q)
            now += cur_task[0]
            answer += now - cur_task[1]
        
        heappush(q, task)

        if now < q[0][1]:
            now = q[0][1]

    while q:
        cur_task = heappop(q)
        now += cur_task[0]
        answer += now - cur_task[1]

    return answer // len(jobs)