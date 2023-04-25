import re

def count_words(string):
    if len(string) == 0:
        raise Exception('Cannot pass empty string!')
    
    string_list = re.findall(r'\w+', string)
    return len(string_list)