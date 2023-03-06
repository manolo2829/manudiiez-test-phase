from letter import Letter

class Word:

    def __init__(self):
        self.word = []
    
    def __repr__(self):
        return f"{self.word}"
    
    
    
    def encode(self, word):
        letterList = list(word)
        auxiliar = []
        for i in range(len(letterList)):
            if not letterList[i] in auxiliar:
                auxiliar.append(letterList[i])
                letter = Letter(letterList[i])
                letter.positions.append(i+1)
                self.word.append(letter)
            else:
                for letter in self.word:
                    if letter.letter == letterList[i]:
                        letter.positions.append(i+1)

    def decode(self, lista):
        print(lista)
        auxiliar = []

        for letter in lista.word: 
            auxiliar = auxiliar + letter.positions
            
        for letter in lista.word:
            for position in letter.positions:
                auxiliar[position-1] = letter.letter

        return "".join(auxiliar)     

    