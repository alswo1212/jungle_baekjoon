def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_sum, pickup_sum = -1, -1
    for i in range(n-1, -1, -1):
        deliver_sum += deliveries[i]
        pickup_sum += pickups[i]

        if deliver_sum >= 0 or pickup_sum >= 0:
            cnt = max(deliver_sum, pickup_sum) // cap + 1
            deliver_sum -= cnt * cap
            pickup_sum -= cnt * cap
            answer += cnt * (i+1)
        
    return answer *  2