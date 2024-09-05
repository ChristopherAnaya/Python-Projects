import random
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
end = False
def rows(x):
    x = int(x) - 1
    a = board[x][0]
    b = board[x][1]
    c = board[x][2]
    if a == 0:
        a = "-"
    elif a == 1:
        a = "X"
    else:
        a = "O"
    if b == 0:
        b = "-"
    elif b == 1:
        b = "X"
    else:
        b = "O"        
    if c == 0:
        c = "-"
    elif c == 1:
        c = "X"
    else:
        c = "O"
    print("           |     |     |     |")
    print("           |  " + str(a) + "  |  " + str(b) + "  |  " + str(c) + "  |")
    print("           |_____|_____|_____|")
def current():
    print("            _________________")
    rows("1")
    rows("2")
    rows("3")
def wins():
    print("--------------------------------------")
    print(" ")
    print("               You Win!               ")
    print(" ")
    print("--------------------------------------")
def loses():
    print("--------------------------------------")
    print(" ")
    print("              You Lose:(              ")
    print(" ")
    print("--------------------------------------")
while end == False:
    current()
    print("--------------------------------------")
    choices = []
    end = False
    while True:
        try:
            row = int(input("Select A Row "))
            if row > 3 or row < 1:
                test = 2/0
            col = int(input("Select A Column "))
            if col > 3 or col < 1:
                test = 2/0
            if board[col-1][row-1] == 0:
                board[col-1][row-1] = 1
            else:
               print("f" + 3)
            print("--------------------------------------")

            break
        except ZeroDivisionError:
            print("--------------------------------------")
            print("     Input Not In Range Try Again     ")
            print("--------------------------------------")

        except TypeError:
            print("--------------------------------------")
            print("Spot On Board Already Filled Try Again")
            print("--------------------------------------")

        except:
            print("--------------------------------------")
            print("     Input Not A Number Try Again     ")
            print("--------------------------------------")
    win = True
    for x in range(3):
        for y in range(3):
            if board[x][y] != 1:
                win = False
        if win == True:
            end = True
            wins()
            break
        win = True
    for x in range(3):
        for y in range(3):
            if board[y][x] != 1:
                win = False
        if win == True:
            end = True
            wins()
            break
        win = True
    for x in range(3):
        if board[x][x] != 1:
            win = False
    if win == True:
        end = True
        wins()
        break
    win = True
    side = 2
    for x in range(3):
        if board[x][side] != 1:
            win = False
        side -= 1
    if win == True:
        end = True
        wins()
        break
    win = False
    tie = True
    for x in board:
        for y in x:
            if y == 0:
                tie = False
    if tie == True:
        end = True
        print("--------------------------------------")
        print(" ")
        print("               You Tied               ")
        print(" ")
        print("--------------------------------------")
        break
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                choices.append([x, y])
    point = random.choice(choices)
    board[point[0]][point[1]] = 2
    lose = True
    for x in range(3):
        for y in range(3):
            if board[x][y] != 2:
                lose = False
        if lose == True:
            end = True
            loses()
            break
        lose = True
    for x in range(3):
        for y in range(3):
            if board[y][x] != 2:
                lose = False
        if lose == True:
            end = True
            loses()
            break
        lose = True
    for x in range(3):
        if board[x][x] != 2:
            lose = False
    if lose == True:
        end = True
        loses()
        break
    lose = True
    side = 2
    for x in range(3):
        if board[x][side] != 2:
            lose = False
        side -= 1
    if lose == True:
        end = True
        loses()
        break
    lose = False
    tie = True
    for x in board:
        for y in x:
            if y == 0:
                tie = False
    if tie == True:
        end = True
        print("--------------------------------------")
        print(" ")
        print("               You Tied               ")
        print(" ")
        print("--------------------------------------")
        break
current()  
