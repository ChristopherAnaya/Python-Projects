letters = list("ABCDEFGHIJKLMNOPQRSTUVWQYZ")
def sort_by_exclusion(words):
    print(words)
    first = sorted(words)[0][0]
    del words[words.index(sorted(words)[0])]
    print(letters.index(first))
    print(first)
    del letters[:letters.index(first)]
    del letters[letters.index(first)]
    print(letters)
    print(words)


print(sort_by_exclusion(["THE","QUICK","BROWN","FOX","JUMPS","OVER","THE","LAZY","DOG"]))