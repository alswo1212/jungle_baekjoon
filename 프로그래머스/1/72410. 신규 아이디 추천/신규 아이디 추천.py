import re
def solution(new_id:str):
    new_id = new_id.lower()
    new_id = re.compile('[^a-z0-9-_.]').sub("", new_id)
    new_id = re.compile('\.{2,}').sub(".", new_id)
    new_id = new_id.removeprefix('.').removesuffix('.')
    if new_id == '': new_id = 'a'
    if len(new_id) >= 16: new_id = new_id[:15]
    new_id = new_id.removesuffix('.')
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id