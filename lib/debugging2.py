def get_most_common_letter(text):
    no_spaces = text.replace(' ', '')
    counter = {}
    for char in no_spaces:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]
    return letter

print(get_most_common_letter("the roof, the roof, the roof is on fire!")) 