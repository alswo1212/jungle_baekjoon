def solution(s:str):
    word_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    pars = s
    for word in word_map.keys():
        pars = pars.replace(word, word_map[word])
    return int(pars)