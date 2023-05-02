import pytest
from unittest.mock import Mock
from lib.sec_diary import *

"""
1. Create mock Dairy object
2. Set object variables
3. Create new SecretDiary object
4. Attempt to read locked SecretDiary | raise exception
"""
def test_read_secret_diary_locked():
    f_diary = Mock()
    f_diary.content = "blah blah blah"
    f_diary.locked = True
    f_sdiary = SecretDiary(f_diary)
    with pytest.raises(Exception) as e:
        f_sdiary.read()
    e_msg = str(e.value)
    assert e_msg == "Go away!"
    

"""
1. Create mock Dairy object
2. Set object variables
3. Create new SecretDiary object
4. Attempt to read unlocked SecretDiary | return string
"""
def test_read_secret_diary_unlocked():
    f_diary = Mock()
    f_diary.content = "blah blah blah"
    f_diary.locked = False
    f_sdiary = SecretDiary(f_diary)
    assert f_sdiary.read() == f_diary.content


"""
1. Create mock Dairy object
2. Set object variables
3. Create new SecretDiary object
4. Attempt to read unlocked SecretDiary | return string
5. Use lock to set SecretDiary to locked
6. Attempt to read locked SecretDiary | raise exception
"""
def test_set_secret_diary_to_locked():
    f_diary = Mock()
    f_diary.content = "blah blah blah"
    f_diary.locked = False
    f_sdiary = SecretDiary(f_diary)
    assert f_sdiary.read() == f_diary.content
    
    f_sdiary.lock()
    with pytest.raises(Exception) as e:
        f_sdiary.read()
    e_msg = str(e.value)
    assert e_msg == "Go away!"


"""
1. Create mock Dairy object
2. Set object variables
3. Create new SecretDiary object
4. Attempt to read locked SecretDiary | raise exception
5. Use unlock to set SecretDiary to unlocked
6. Attempt to read unlocked SecretDiary | raise string
"""
def test_set_secret_diary_to_unlocked():
    f_diary = Mock()
    f_diary.content = "blah blah blah"
    f_diary.locked = True
    f_sdiary = SecretDiary(f_diary)
    with pytest.raises(Exception) as e:
        f_sdiary.read()
    e_msg = str(e.value)
    assert e_msg == "Go away!"
    
    f_sdiary.unlock()
    assert f_sdiary.read() == f_diary.content


"""
1. Create mock Dairy object
2. Set object variables
3. Create new SecretDiary object
4. Attempt to lock already locked SecretDiary | raise exception
"""
def test_set_secret_diary_to_locked_already_locked():
    f_diary = Mock()
    f_diary.content = "blah blah blah"
    f_diary.locked = True
    f_sdiary = SecretDiary(f_diary)
    with pytest.raises(Exception) as e:
        f_sdiary.lock()
    e_msg = str(e.value)
    assert e_msg == "Already locked"


"""
1. Create mock Dairy object
2. Set object variables
3. Create new SecretDiary object
4. Attempt to unlock already unlocked SecretDiary | raise exception
"""
def test_set_secret_diary_to_unlocked_already_unlocked():
    f_diary = Mock()
    f_diary.content = "blah blah blah"
    f_diary.locked = False
    f_sdiary = SecretDiary(f_diary)
    with pytest.raises(Exception) as e:
        f_sdiary.unlock()
    e_msg = str(e.value)
    assert e_msg == "Already unlocked"
