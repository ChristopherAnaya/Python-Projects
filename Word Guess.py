import random
bank = ["disco", "requirement", "freshman", "courtesy", "vertical", "contact", "important", "discover", "influence", "absent", "joystick", "wilderness"]
word = random.choice(bank)
wordlisted = list(word)
empty = ""
for x in wordlisted:
    empty += "_"
chances = 10
dupetest = word
wrong = ""
solved = len(word)
stop = 1
print("The word is " + str(len(word)) + " letters long.")
while stop > 0:
    letter = str(input("Choose a letter"))
    if letter in word:
        if letter in dupetest:
            for x in dupetest:
                if letter in dupetest:
                    location = dupetest.find(letter)
                    emptylist = list(empty)
                    emptylist[location] = letter
                    empty = "".join(emptylist)
                    wordlisted[location] = " "
                    dupetest = "".join(wordlisted)
                    solved -= 1
            print("Your wrong letters are " + wrong)
            print("You have " + str(chances) + " chances left")
            print(empty)
        else:
            print("You already guessed this letter")
    else:
        if letter in wrong:
            print("You already guessed this letter")
        else:
            wrong = wrong + letter
            chances -= 1
            print("Your wrong letters are " + wrong)
            print("You have " + str(chances) + " chances left")
            print(empty)
    if solved == 0:
        stop = 0
    if chances == 0:
        stop = 0
if solved == 0:
    print("You win")
if chances == 0:
    print("You lose the word was " + word + ".")
