import sys

n = int(input())
max = 10_000
is_not_prime = [False] * max

for i in range(2, 5000):
    for j in range(i + i, max, i):
        is_not_prime[j] = True

is_not_prime[0] = is_not_prime[1] = True

def get_goldbach_partition(num):
    result_small_prime = 0
    result_big_prime = num

    for i in range(2, num // 2 + 1):
        if is_not_prime[i] : continue
        if is_not_prime[num - i] : continue
        
        small_prime = i
        big_prime = num - i
        if (result_big_prime - result_small_prime) > (big_prime - small_prime):
            result_small_prime = small_prime
            result_big_prime = big_prime

    return result_small_prime, result_big_prime

results = []
for i in range(n):
    input_num = int(sys.stdin.readline())
    prime1, prime2 = get_goldbach_partition(input_num)
    results.append(f'{prime1} {prime2}')

print('\n'.join(results))