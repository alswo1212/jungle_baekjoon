import re
input()
s = input().strip()
result = sum(int(c) for c in re.split('[a-zA-Z]+', s) if c != '')
print(result)