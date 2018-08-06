from classes import Word
import string

def find_words(list_of_words):
    letters = list(string.ascii_lowercase)
    words = []
    for word in list_of_words:
        for l in letters:
            new = word.add_letter(l)
            if len(new) > 0:
                words = words + new
            new = []

    return words

def largest_word_len(list_of_words):
    count = 0
    for word in list_of_words:
        if word.wordLength > count:
            count = word.wordLength
    return count

masterlist = [Word("a")]
count = 0

while count < 8:
    masterlist = find_words(masterlist)
    count = largest_word_len(masterlist)

for w in masterlist:
    print w.currentWord
    print w.index_order

f = open("results.txt", 'w')
for w in masterlist:
    f.write(w.currentWord)
    f.write("\n")
    for index in w.index_order:
        f.write("%d" % index)
        f.write(",")
    f.write("\n")
