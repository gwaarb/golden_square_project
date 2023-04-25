# Reading Time Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
    def reading_time(text):
        # Parameters:
        #   text: a string containing words
        # Return:
        #   a string containing the time it estimates to read the given text
        # E.g. "The reading time for {number of words} words is {estimated time}."
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
If we pass a parameter that is not a string
It will raise an exception
"""
> reading_time(False)
> # => "The passed arguement was not Type: String."

"""
If we pass an empty string
It will raise an exception 
"""
> reading_time('')
> # => "The string did not contain any text."

"""
If we pass a string containing less than 200 words
It will return a string advising a minimum reading time
"""
> reading_time(150_words)
> # => "The reading time for 150 words is less than a minute."

"""
If we pass a string containing 200 words
It will return a string advising a minimum reading time
"""
> reading_time(200_words)
> # => "The reading time for 200 words is 1.0 minute(s)."

"""
If we pass a string containing 250 words
It will return a string advising the estimated time in minutes
"""
> reading_time(250_words)
> # => "The reading time for 200 words is 1.25 minute(s)."

"""
If we pass a string containing 431 words
It will return a string advising the estimated time in minutes
"""
> reading_time(431_words)
> # => "The reading time for 431 words is 2.15 minute(s)."

"""
If we pass a string containing 12000 words
It will return a string advising the estimated time in hours
"""
> reading_time(12000_words)
> # => "The reading time for 12000 words is 1.00 hour(s)."

"""
If we pass a string containing 12899 words
It will return a string advising the estimated time in hours
"""
> reading_time(12899_words)
> # => "The reading time for 12899 words is 1.07 hour(s)."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
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
```

Ensure all test function names are unique, otherwise pytest will ignore them!