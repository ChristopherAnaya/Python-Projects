import tkinter as tk

window = tk.Tk()
window.title("Ping Pong")
window.resizable(False, False)

canvas = tk.Canvas(window, width=340, height=340, bg="gray")
canvas.pack()

box1 = canvas.create_rectangle(20, 20, 120, 120, fill="grey", width = 2)
box2 = canvas.create_rectangle(120, 20, 220, 120, fill="grey", width = 2)
box3 = canvas.create_rectangle(220, 20, 320, 120, fill="grey", width = 2)
box4 = canvas.create_rectangle(20, 120, 120, 220, fill="grey", width = 2)
box5 = canvas.create_rectangle(120, 120, 220, 220, fill="grey", width = 2)
box6 = canvas.create_rectangle(220, 120, 320, 220, fill="grey", width = 2)
box7 = canvas.create_rectangle(20, 220, 120, 320, fill="grey", width = 2)
box8 = canvas.create_rectangle(120, 220, 220, 320, fill="grey", width = 2)
box9 = canvas.create_rectangle(220, 220, 320, 320, fill="grey", width = 2)
import random
board = []
size = 3
for x in range(size):
    hold = []
    for y in range(size):
        hold.append("-")
    board.append(hold)
def rows(x, y):
    canvas.create_line(20*x, 20*y, 120*x, 120*y, fill="black", width=5) 
    canvas.create_line(120*x, 20*y, 20*x, 120*y, fill="black", width=5)
def current():
    for x in range(3):
        for y in range(3):
            if board[x][y] == "X":
                rows(x,y)
                print(x,y)
    
    window.after(1000, window.close)
    window.mainloop()

while True:
    try:
        players = int(input("How Many Players "))
        if players > 2 or players <= 0:
            2/0
        break
    except ZeroDivisionError:
        print("--------------------------------------")
        print("  To Many Or Little Players Try Again ")
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
