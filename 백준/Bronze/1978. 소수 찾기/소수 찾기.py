input()
nums = map(int, input().split())

def is_prime(num):
    if num == 1 : return False

    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0: return False

    return True

primes = list(filter(is_prime, nums))
print(len(primes))