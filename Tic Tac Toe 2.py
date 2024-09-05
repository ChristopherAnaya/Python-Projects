import random
board = []
while True:
    try:
        size = int(input("Choose Your Size "))
        size + 1
        if size <= 2:
            2/0
        break
    except ZeroDivisionError:
        print("--------------------------------------")
        print("     Input Not In Range Try Again     ")
        print("--------------------------------------")
    except:
        print("--------------------------------------")
        print("     Input Not A Number Try Again     ")
        print("--------------------------------------")
for x in range(size):
    hold = []
    for y in range(size):
        hold.append("-")
    board.append(hold)
def rows(y):
    top = "|"
    mid = "|  "
    bot = "|"
    for x in range(size):
        top += "     |"
        mid += str(board[y][x]) + "  |  "
        bot += "_____|"
    print(top)
    print(mid)
    print(bot)
def current():
    top = " "
    for x in range(size):
        if x == 0:
            top += "_____"
        else:
            top += "______"
    print(top)
    for x in range(size):
        rows(x)

while True:
    try:
        players = int(input("How Many Players "))
        if players > 2:
            2/0
        break
    except ZeroDivisionError:
        print("--------------------------------------")
        print("       To Many Players Try Again      ")
        print("--------------------------------------")
    except:
        print("--------------------------------------")
        print("     Input Not A Number Try Again     ")
        print("--------------------------------------")
if players == 1:
    while True:
        try:
            side = input("Choose X or O ")
            side = side.upper()
            if side != "X" and side != "O":
                2/0
            break
        except ZeroDivisionError:
            print("--------------------------------------")
            print("      Input Not X or O Try Again      ")
            print("--------------------------------------")
else:
    side = "X"
def player(y):
    while True:
        try:
            row = int(input("Select A Row "))
            if row > size or row < 1:
                test = 2/0
            col = int(input("Select A Column "))
            if col > size or col < 1:
                test = 2/0
            if board[col-1][row-1] == "-":
                board[col-1][row-1] = y
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
def enemy(z):
    z = "X" if z == "O" else "O"
    choices = []
    for x in range(size):
        for y in range(size):
            if board[x][y] == "-":
                choices.append([x, y])
    point = random.choice(choices)
    board[point[0]][point[1]] = z
def tied():
    tie = True
    for x in board:
        for y in x:
            if y == "-":
                tie = False
    if tie == True:
        end = True
        print("--------------------------------------")
        print(" ")
        print("               You Tied               ")
        print(" ")
        print("--------------------------------------")
        return "break"
def X_Wins():
    if players == 1:
        if side == "X":
            print("--------------------------------------")
            print(" ")
            print("               You Win!               ")
            print(" ")
            print("--------------------------------------")
        else:
            print("--------------------------------------")
            print(" ")
            print("              You Lose:(              ")
            print(" ")
            print("--------------------------------------")
    else:
            print("--------------------------------------")
            print(" ")
            print("                X Wins!                ")
            print(" ")
            print("--------------------------------------")
def O_Wins():
    if players == 1:
        if side == "O":
            print("--------------------------------------")
            print(" ")
            print("               You Win!               ")
            print(" ")
            print("--------------------------------------")
        else:
            print("--------------------------------------")
            print(" ")
            print("              You Lose:(              ")
            print(" ")
            print("--------------------------------------")
    else:
            print("--------------------------------------")
            print(" ")
            print("                O Wins!                ")
            print(" ")
            print("--------------------------------------")
def X_Win():
    win = True
    for x in range(size):
        for y in range(size):
            if board[x][y] != "X":
                win = False
        if win == True:
            end = True
            X_Wins()
            return "break"
        win = True
    for x in range(size):
        for y in range(size):
            if board[y][x] != "X":
                win = False
        if win == True:
            end = True
            X_Wins()
            return "break"
        win = True
    for x in range(size):
        if board[x][x] != "X":
            win = False
    if win == True:
        end = True
        X_Wins()
        return "break"
    win = True
    side = size - 1
    for x in range(size):
        if board[x][side] != "X":
            win = False
        side -= 1
    if win == True:
        end = True
        X_Wins()
        return "break"
def O_Win():
    win = True
    for x in range(size):
        for y in range(size):
            if board[x][y] != "O":
                win = False
        if win == True:
            end = True
            O_Wins()
            return "break"
        win = True
    for x in range(size):
        for y in range(size):
            if board[y][x] != "O":
                win = False
        if win == True:
            end = True
            O_Wins()
            return "break"
        win = True
    for x in range(size):
        if board[x][x] != "O":
            win = False
    if win == True:
        end = True
        O_Wins()
        return "break"
    win = True
    side = size - 1
    for x in range(size):
        if board[x][side] != "O":
            win = False
        side -= 1
    if win == True:
        end = True
        O_Wins()
        return "break"
while True:
    if players == 1:
        if side == "X":
            current()
            player(side)
        else:
            enemy(side)
        if X_Win() == "break":
            break
        if tied() == "break":
            break
        if side == "X":
            enemy(side)
        else:
            current()
            player(side)
        if O_Win() == "break":
            break
        if tied() == "break":
            break
    else:
        current()
        player("X")
        if X_Win() == "break":
            break
        if tied() == "break":
            break
        current()
        player("O")
        if O_Win() == "break":
            break
        if tied() == "break":
            break
current()


    
