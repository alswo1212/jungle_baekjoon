s = input().strip()

if s[0] != '0':
    print(s)
else:
    s = s[1:]
    result = 0
    if s[0] == 'x':
        s = s[1:]
        po = len(s) - 1
        for c in s:
            if c >= 'a':
                result += (ord(c) - 87) * (16 ** po)
            else:
                result += int(c) * (16 ** po)
            po -= 1
    else:
        po = len(s) - 1
        for c in s:
            result += int(c) * (8 ** po)
            po -= 1
    print(result)