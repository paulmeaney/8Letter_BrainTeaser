import enchant
import string


dict = enchant.Dict("en_UK")   # create dictionary for US English

letters = list(string.ascii_lowercase)
outputword = []
nextletter = 1
currletter = 0

postion = 0



while (len(outputword) < 8):
    while currletter < len(letters) - 1:
        while (postion < len(outputword)-1): #for i in range(len(outputword)-1): #position
            outputword.insert(position, letters[currletter])
            position = position + 1
            #is it a word?
            if (dict.check(''.join(outputword))):
                currletter = 0
                break
            del outputword[postion - 1]
        currletter = currletter + 1




print ''.join(outputword)
