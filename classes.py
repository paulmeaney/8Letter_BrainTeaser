import string
import enchant #this library contains a dictionary
class Word:
    dict = enchant.Dict("en_US")

    def __init__(self, inputWord):
        self.currentWord = inputWord

    def check_if_valid_word(self, word):
        return self.dict.check(word)


    def add_letter(self, letter):
        str_list = list(self.currentWord)
        valid_words = []
        for i in range(0, len(str_list)+1):
            str_list.insert(i, letter)
            if self.check_if_valid_word(''.join(str_list)):
                valid_words.append(Word(''.join(str_list)))

            del str_list[i]

        return valid_words
