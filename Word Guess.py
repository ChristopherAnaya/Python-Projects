import random
bank = ["disco", "requirement", "freshman", "courtesy", "vertical", "contact", "important", "discover", "influence", "absent", "joystick", "wilderness"]
word = random.choice(bank)
wordlisted = list(word)
empty = ""
for x in wordlisted:
    empty += "_"
chances = 5
wrong = ""
solved = len(word)
stop = 1
print("The word is " + str(len(word)) + " letters long.")
print(word)



if solved == 0:
    print("You win")
if chances == 0:
    print("You lose")
