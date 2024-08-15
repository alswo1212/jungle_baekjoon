num = int(input())
result = ''
if 620 <= num <= 780:
    result = 'Red'
elif 590 <= num < 620:
    result = 'Orange'
elif 570 <= num < 590:
    result = 'Yellow'
elif 495 <= num < 570:
    result = 'Green'
elif 450 <= num < 495:
    result = 'Blue'
elif 425 <= num < 450:
    result = 'Indigo'
elif 380 <= num < 425:
    result = 'Violet'

print(result)