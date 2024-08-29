def bomb_has_been_planted(m, time):
    kloc = []
    the_return = True
    for x in range(len(m)):
        for y in range(len(m[0])):
            if m[x][y] == "CT":
                ctloc = [x,y]
            if m[x][y] == "B":
                bloc = [x,y]
            if m[x][y] == "K":
                kloc = [x,y]
    dist = 0
    while ctloc[0] != bloc[0] and ctloc[1] != bloc[1]:
        if ctloc[0] < bloc[0] and ctloc[1] < bloc[1]:
            ctloc[0] += 1
            ctloc[1] += 1
            dist += 1
        if ctloc[0] < bloc[0] and ctloc[1] > bloc[1]:
            ctloc[0] += 1
            ctloc[1] -= 1
            dist += 1
        if ctloc[0] > bloc[0] and ctloc[1] < bloc[1]:
            ctloc[0] -= 1
            ctloc[1] += 1
            dist += 1
        if ctloc[0] > bloc[0] and ctloc[1] > bloc[1]:
            ctloc[0] -= 1
            ctloc[1] -= 1
            dist += 1
    dist += abs(ctloc[0] - bloc[0]) + abs(ctloc[1] - bloc[1])
    if dist + 10 > time:
        the_return = False
        print("fail")
    else:
        return True
    if the_return == False:
        if kloc != []:
            dist = 0
            while ctloc[0] != kloc[0] and ctloc[1] != kloc[1]:
                if ctloc[0] < kloc[0] and ctloc[1] < kloc[1]:
                    ctloc[0] += 1
                    ctloc[1] += 1
                    dist += 1
                if ctloc[0] < kloc[0] and ctloc[1] > kloc[1]:
                    ctloc[0] += 1
                    ctloc[1] -= 1
                    dist += 1
                if ctloc[0] > kloc[0] and ctloc[1] < kloc[1]:
                    ctloc[0] -= 1
                    ctloc[1] += 1
                    dist += 1
                if ctloc[0] > kloc[0] and ctloc[1] > kloc[1]:
                    ctloc[0] -= 1
                    ctloc[1] -= 1
                    dist += 1
            print(dist)
            dist += abs(ctloc[0] - kloc[0]) + abs(ctloc[1] - kloc[1])
            print(dist)


        else:
            return False










print(bomb_has_been_planted([
            ["0", "0", "0", "0", "0", "0"],
            ["CT", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "B"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "K", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"]
        ], 13))
