class SecretDiary:
    def __init__(self, diary):
        self.diary = diary

    def read(self):
        if self.diary.locked == True:
            raise Exception("Go away!")
        return self.diary.content

    def lock(self):
        if self.diary.locked:
            raise Exception("Already locked")
        self.diary.locked = True

    def unlock(self):
        if not self.diary.locked:
            raise Exception("Already unlocked")
        self.diary.locked = False