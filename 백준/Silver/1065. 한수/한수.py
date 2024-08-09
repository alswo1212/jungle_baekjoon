def is_hansu(num):
    if num < 100 : return True

    term = num % 100 // 10 - num % 10
    
    while num > 9:
        dif = num % 100 // 10 - num % 10
        if dif != term : return False
        num //= 10

    return True

result = len(list(filter(is_hansu, map(lambda n: n + 1, range(int(input()))))))
print(result)
