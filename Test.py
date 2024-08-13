def find_glasses(lst):
    lst = [x.lower() for x in lst]
    empty = []
    stop = 0
    lose = False
    for x in lst:
        hold = x
        if "o" in x:
            position = x.find("o")
            x = list(x)
            useless = x.pop(position)
            x = "".join(x)
            position_2 = x.find("o") + 1
            for x in range(position + 1, position_2):
                stop += 1
                print(stop)
            for y in range(position + 1, position_2):
                while stop > 0:
                    if hold[y] == "-":
                        stop -= 1
                    else:
                        stop = 0
                        lose = True
            if lose == True:
                lose = False
            else:
                empty.append(hold)
    return empty
print(find_glasses(["O--O", "O----d-O"]))
