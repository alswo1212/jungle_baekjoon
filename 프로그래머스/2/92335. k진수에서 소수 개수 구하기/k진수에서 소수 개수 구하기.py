def solution(n, k):
    def is_prime(num:int)->bool:
        if num < 2:
            return False
        if num <= 3:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    answer = 0
    nums = []
    while n:
        nums.append(str(n % k))
        n //= k
    for num in ''.join(nums[::-1]).split('0'):
        if num == '':
            continue
        if is_prime(int(num)):
            answer += 1
    return answer