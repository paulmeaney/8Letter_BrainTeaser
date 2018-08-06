from classes import Word

sample = Word("coast")

new_words = sample.add_letter('s')

if (len(new_words) == 0):
    print "no words"
for word in new_words:
    print word.currentWord
