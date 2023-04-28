class Entry():
    title, entry, mob = str, str, str
    def __init__(self, title, entry, mob=''):
        if not isinstance(title, str) or not title.strip():
            raise Exception('Invalid Title')
        if not isinstance(entry, str) or not entry.strip():
            raise Exception('Invalid Entry')
        self.title = title
        self.entry = entry
        self.mob = mob