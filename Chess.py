board = [["r", "n", "b", "q", "k", "b", "n", "r"], ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "p", "-", "-", "-", "-", "-", "-"],
         ["P", "P", "P", "P", "P", "P", "P", "P"], ["R", "N", "B", "Q", "K", "B", "N", "R"]]
def rows(y):
    top = "|"
    mid = "|  "
    bot = "|"
    for x in range(8):
        top += "     |"
        mid += str(board[y][x]) + "  |  "
        bot += "_____|"
    print(top)
    print(mid)
    print(bot)
def current():
    top = " "
    for x in range(8):
        if x == 0:
            top += "_____"
        else:
            top += "______"
    print(top)
    for x in range(8):
        rows(x)
convert = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0, "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
whitepieces = ["P", "R", "N", "B", "K", "Q"]
blackpieces = ["p", "r", "n", "b", "k", "q"]
whitepromo = ["R", "N", "B", "Q"]
blackpromo = ["r", "n", "b", "q"]
promo = {"a":["b"], "b":["a","c"], "c":["b","d"], "d":["c","e"], "e":["d","f"], "f":["e","g"], "g":["f","h"], "h":["g"]}
def pawn(x, y):
    if turn == "white":
        if board[convert[x[1]]][convert[x[0]]] == "P":
            if x[1] == "2":
                print(1)
                return True if int(y[1]) < 5 and int(y[1]) > 2 and board[convert[y[1]]][convert[y[0]]] == "-" and x[0] == y[0] or board[convert[y[1]]][convert[y[0]]] in blackpieces and promo[x[0]][0] == y[0] and x[1] == x[1] + 1 or board[convert[y[1]]][convert[y[0]]] in blackpieces and promo[x[0]][1] == y[0] and x[1] == x[1] + 1 else False
            elif int(x[1]) < 7:
                print(2)
                return True if int(y[1]) == int(x[1]) + 1 and board[convert[y[1]]][convert[y[0]]] == "-" and x[0] == y[0] or board[convert[y[1]]][convert[y[0]]] in blackpieces and promo[x[0]][0] == y[0] and x[1] == x[1] + 1 or board[convert[y[1]]][convert[y[0]]] in blackpieces and promo[x[0]][1] == y[0] and x[1] == x[1] + 1 else False
            else:
                print(3)
                if int(y[1]) == int(x[1]) + 1 and board[convert[y[1]]][convert[y[0]]] == "-" and x[0] == y[0] or board[convert[y[1]]][convert[y[0]]] in blackpieces and promo[x[0]][0] == y[0] and x[1] == x[1] + 1 or board[convert[y[1]]][convert[y[0]]] in blackpieces and promo[x[0]][1] == y[0] and x[1] == x[1] + 1:
                    return "promote"
                else:
                    False
        else:
            return True

def logic(x, y):
    hold = pawn(x, y)
    if hold == False:
        return "error"
    elif hold == "promote":
        return "promote"

def player():
    while True:
        try:
            start = input("Select A Piece ")
            if board[convert[start[1]]][convert[start[0]]] == "-":
                raise ValueError("Spot On Board Empty")
            if board[convert[start[1]]][convert[start[0]]] in whitepieces and turn == "black":
                raise ValueError("This Is Not Your Piece")
            if board[convert[start[1]]][convert[start[0]]] in blackpieces and turn == "white":
                raise ValueError("This Is Not Your Piece")
            end = input("Select A Location ")
            if board[convert[end[1]]][convert[end[0]]] in whitepieces and turn == "white":
                raise ValueError("Cannot Move On To Your Own Pieces")
            if board[convert[end[1]]][convert[end[0]]] in blackpieces and turn == "black":
                raise ValueError("Cannot Move On To Your Own Pieces")
            piece = board[convert[start[1]]][convert[start[0]]]

            log = logic(start, end)
            print(log)
            if log == "error":
                raise ValueError("Not A Valid Move or Not Valid Notation")
            if log == "promote":
                while True:
                    try:
                        piece = input("What Piece Would You Like To Promote To? ").upper()
                        if turn == "white":
                            if piece not in whitepromo:
                                raise ValueError("Not Valid ")
                            board[convert[end[1]]][convert[end[0]]] = piece.upper()
                            board[convert[start[1]]][convert[start[0]]] = "-"
                            break
                        if turn == "black":
                            if piece not in blackpromo:
                                raise ValueError("Not Valid ")
                            board[convert[end[1]]][convert[end[0]]] = piece
                            board[convert[start[1]]][convert[start[0]]] = "-"
                            break
                    except ValueError as x:
                        print(x)
            else:
                board[convert[end[1]]][convert[end[0]]] = board[convert[start[1]]][convert[start[0]]]
                board[convert[start[1]]][convert[start[0]]] = "-"
            break
        except ValueError as x:
            print(x)
        except:
            print("Not A Valid Move or Not Valid Notation")
while True:
    turn = "white"
    current()
    player()
    '''turn = "black"
    current()
    player()'''













    
