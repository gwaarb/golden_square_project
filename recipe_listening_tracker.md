# Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
    class Runman()
        # initialise: empty track list

        # add function:
            # Arguements > string for track name
            # Validation of string > check is string, not empty or whitespace
            # Return track added message
        
        # review function:
            # No arguements
            # Returns list values formatted into string
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Add method > check is valid string - not empty, not whitespace, IS string
Raises exception
"""
def test_track_name_is_valid():
    runman = Runman()
    with pytest.raises(Exception) as e:
        runman.add('')
    e_msg = str(e.value)
    assert e_msg == "Invalid string"

    with pytest.raises(Exception) as e:
        runman.add(10)
    e_msg = str(e.value)
    assert e_msg == "Invalid string"

    with pytest.raises(Exception) as e:
        runman.add(None)
    e_msg = str(e.value)
    assert e_msg == "Invalid string"

    with pytest.raises(Exception) as e:
        runman.add(' ')
    e_msg = str(e.value)
    assert e_msg == "Invalid string"

"""
Add method > pass track name as stirng
Returns formatted message
"""
def test_track_added():
    runman = Runman()
    res = runman.add('Stayin Alive')
    assert res == "Track Added: Stayin Alive

"""
Review method > no arguements
Returns formatted message
"""
def test_review_tracks():
    runman = Runman()
    runman.add('Stayin Alive')
    runman.add('Barbie Girl')
    runman.add('Numb')
    res = runman.review()
    assert res == "Listened Tracks: Stayin Alive, Barbie Girl, Numb"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
    class Runman():
        
        def __init__(self):
            self.track_list = []

        def add(self, track):
            if not isinstance(track, str) or not track.strip():
                raise Exception("Invalid string")
            self.track_list.append(track)
            return f"Track Added: {track}" 

        def review(self):
            track_string = ", ".join(self.track_list)
            return f"Listened Tracks: {track_string}"
```

Ensure all test function names are unique, otherwise pytest will ignore them!