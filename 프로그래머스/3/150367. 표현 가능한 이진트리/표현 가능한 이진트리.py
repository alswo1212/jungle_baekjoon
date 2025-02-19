def solution(numbers):
    def num_2_bi(num:int)->str:
        result = ''
        cnt = 1
        right = 1
        while num > right:
            cnt = (cnt << 1) + 1
            right = 1 << cnt

        while cnt > 0:
            result += str(num % 2)
            num >>= 1
            cnt -= 1
        return result
    
    def check_tree(bi_num:str)->bool:
        n = len(bi_num)
        if n <= 1 or int(bi_num) == 0:
            return True
        
        if bi_num[n//2] == '0':
            return False
        return check_tree(bi_num[0:n//2]) and check_tree(bi_num[n//2+1:])
    
    answer = []
    for num in numbers:
        answer.append(1 if check_tree(num_2_bi(num)) else 0)
    return answer