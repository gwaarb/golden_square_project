class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        # while i < len(self.text):
        #    if self.text[i].lower() in self.vowels:
        #        self.text = self.text[:i] + self.text[i+1:]
        #    i += 1
        no_vowels = [char for char in self.text if char not in self.vowels]
        return "".join(no_vowels)
    
remover = VowelRemover("burp the kimchee")
print(remover.remove_vowels())