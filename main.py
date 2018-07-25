import enchant
import string
dict = enchant.Dict("en_US")   # create dictionary for US English

letters = list(string.ascii_lowercase)
outputword = []
nextletter = ''
currletter = 'a'

while (len(outputword) < 8):
    nextletter = currletter
    outputword.insert(0, nextletter)
    #is it a word?
    


print ''.join(outputword)
