import re

def reading_time(text):
    if not isinstance(text, str):
        raise Exception("The passed arguement was not Type: String.")
    if len(text) < 1:
        raise Exception("The string did not contain any text.")
    
    words = re.split(r"\w+", text)
    wpm = 200 # words per minute
    txt_len = len(words)
    if txt_len < 200:
        return f"The reading time for {txt_len} words is less than a minute."

    # rt - reading time
    rt_seconds = txt_len / wpm * 60
    rt_mins = rt_seconds / 60
    if rt_mins >= 60:
        rt_hours = rt_mins / 60 
        rt_string = f"{rt_hours:.2f} hour(s)"
    else:
        rt_string = f"{rt_mins:.2f} minute(s)"
    
    return f"The reading time for {txt_len} words is {rt_string}."
