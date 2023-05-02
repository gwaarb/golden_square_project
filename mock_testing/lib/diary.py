class Diary:
    content = str
    locked = bool
    def __init__(self, contents):
        if not isinstance(contents, str) or not contents.strip():
            raise Exception("Invalid contents")
        self.content = contents
        self.locked = False

    def read(self): return self.content