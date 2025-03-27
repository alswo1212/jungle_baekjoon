def solution(files):
    def file_sort_func(file_name:str):
        head, number = '', 0
        left, right = 0, 0
        for i in range(len(file_name)):
            if file_name[i].isdigit() and left == 0:
                head = file_name[:i].upper()
                left = i
            elif not file_name[i].isdigit() and left != 0:
                right = i
                number = int(file_name[left:right])
                break
            
        if right == 0:
            number = int(file_name[left:])

        return (head, number)
    
    return sorted(files, key=file_sort_func)