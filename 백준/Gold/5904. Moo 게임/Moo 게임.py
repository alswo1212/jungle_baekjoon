target = int(input())

def moo(target, depth, side_len):
    if target <= 3:
        return 'm' if target == 1 else 'o'
    
    if side_len < target <= side_len + depth + 3:
        return 'm' if (target - side_len) == 1 else 'o'
    
    total_len = side_len * 2 + depth + 3
    if total_len < target:
        return moo(target, depth + 1, total_len)
    
    before_len = (side_len - (depth - 1) - 3) >> 1
    if target <= side_len:
        return moo(target, depth - 1, before_len)
    else :
        return moo(target - side_len - depth - 3, depth - 1, before_len)

print(moo(target, 0, 0))