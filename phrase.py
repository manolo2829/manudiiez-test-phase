from word import Word

class Phrase:

    def __init__(self):
        self.encoded = []
        self.lista = []

    def __repr__(self):
        return f"{self.encoded}"
    
    @property
    def decoded(self):
        return " ".join(self.lista)
    
    def encode(self, phrase):
        wordList = phrase.split(' ')
        for each in wordList:
            word = Word()
            word.encode(each)
            self.encoded.append(word)
        
    def decode(self, lista):
        for each in lista:
            word = Word()
            self.lista.append(word.decode(each))

