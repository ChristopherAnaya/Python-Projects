def find_glasses(lst):
    lst = [x.lower() for x in lst]
    empty = []
    stop = 1
    lose = 1
    for x in lst:
        hold = x
        while stop > 0:
            if "o" in x:
                position = x.find("o")
                x = list(x)
                useless = x.pop(position)
                x = "".join(x)
                if "o" in x:
                    position_2 = x.find("o") + 1
                    for z in range(position + 1, position_2):
                        stop += 1
                    while stop > 0:
                        for y in range(position + 1, position_2):
                            if hold[y] != "-":
                                lose = 0
                                break
                        break
                    if lose == 0:
                        lose = 1
                    else:
                        empty.append(hold)
                hold = x
            break
    return empty
print(find_glasses(['phone', 'O-o', 'coins', 'keys']))

