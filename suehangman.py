import random
from wordfile import words       #place words from a file into a list words[]

#print(words)

def get_valid_word(words):
    word = random.choice(words)  #randomly chooses a word from list
    while ' ' in word or '-' in word:
     oops = "trying again, chose {}"
     print(oops.format(word))
     word = random.choice(words)
    return word

#TDD - Trying out hangman blanks display before placing into Real Code..

winnerword = get_valid_word(words)
print()
print(winnerword)
print()
i = len(winnerword)
blanks = " "
while i > 0:
    blanks = blanks + "_ "
    i -= 1
print(blanks)

