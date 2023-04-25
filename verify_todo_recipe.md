# Reading Time Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my tasks
> I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
    def verify_todo(text):
        # Paramaters:
            # string: a string containing words
        # Return:
        #   true or false depending on key word '#TODO' detected
        # E.G. True 
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
If we pass a an arguement that isn't a string
It will raise an exception
"""
> verify_todo(100)
> # => "No text found"

"""
If we pass a an empty string
It will raise an exception
"""
> verify_todo('')
> # => "No text found"

"""
If we pass a string containing "#TODO"
It will return True
"""
> verify_todo('#TODO Wash the dishes')
> # => True

"""
If we pass a string containing "#2do"
It will return False
"""
> verify_todo('#T2do Wash the dishes')
> # => False

"""
If we pass a string containing "#toodo"
It will return False
"""
> verify_todo('#toodo Wash the dishes')
> # => False

"""
If we pass a string containing "#todo"
It will return False
"""
> verify_todo('#todo Wash the dishes')
> # => False

"""
If we pass a string containing "todo"
It will return False
"""
> verify_todo('todo Wash the dishes')
> # => False

"""
If we pass a string containing "TODO"
It will return False
"""
> verify_todo('TODO Wash the dishes')
> # => False

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
    def verify_todo(text):
    if not isinstance(text, str) or not text.strip():
        raise Exception("No text found")
    
    if "#TODO" in text:
        return True
    
    return False
```

Ensure all test function names are unique, otherwise pytest will ignore them!