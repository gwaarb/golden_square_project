def verify_todo(text):
    if not isinstance(text, str) or not text.strip():
        raise Exception("No text found")
    
    if "#TODO" in text:
        return True
    
    return False