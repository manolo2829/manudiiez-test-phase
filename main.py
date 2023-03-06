from phrase import Phrase


if __name__ == '__main__':
    phrase = Phrase()
    phrase.encode('anana de mama')
    result = phrase.encoded
    phrase.decode(result)
    print(phrase.decoded)