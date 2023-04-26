import pytest
from lib.listening_tracker import *

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
    assert res == "Track Added: Stayin Alive"

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