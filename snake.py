import tkinter as tk

window = tk.Tk()
window.title("Pong Game")
window.resizable(False, False)

canvas = tk.Canvas(window, width=600, height=600, bg="gray")
canvas.pack()

points = 0000

pellet = canvas.create_oval(105, 105, 115, 115, fill="lightyellow")
enemy1 = canvas.create_rectangle(222, 202, 238, 218, fill="pink")
player = canvas.create_rectangle(22, 2, 38, 18, fill="yellow")
score = canvas.create_text(560, 10, text= f"Points: {points}", fill="black", font=("Press Start 2P", 12))
heart1 = canvas.create_rectangle(480, 5, 500, 25, fill="red")
heart2 = canvas.create_rectangle(450, 5, 470, 25, fill="red")
heart3 = canvas.create_rectangle(420, 5, 440, 25, fill="red")

enemys = [enemy1]
pellets = [pellet] 
hearts = [heart1, heart2, heart3]

x=0
y=0

def changeS(event):
    global x, y
    y = 20
    x = 0

def changeW(event):
    global x, y
    y = -20
    x = 0

def changeA(event):
    global x, y
    y = 0
    x = -20

def changeD(event):
    global x, y
    y = 0
    x = 20

def playermoves():
    global x, y
    canvas.move(player, x, y)
    x = 0
    y = 0
    window.after(50, playermoves)

def pelletsscore():
    global points
    x1, y1, x2, y2 = canvas.coords(player)
    for p in pellets:
        x3, y3, x4, y4 = canvas.coords(p)
        if x1 <= x3 and x2 >= x4 and y1 <= y3 and y2 >= y4:
            points += 10
            canvas.delete(p)
            del pellets[pellets.index(p)]
    canvas.itemconfig(score, text=f"Points: {points}")
    window.after(50, pelletsscore)

def damage():
    x1, y1, x2, y2 = canvas.coords(player)
    for e in enemys:
        x5, y5, x6, y6 = canvas.coords(e)
        if x1 <= x5 and x2 >= x6 and y1 <= y5 and y2 >= y6:
            print(hearts)
            canvas.delete(hearts[-1])
            del hearts[-1]
    window.after(50, damage)

def currentcords(event):
    print(canvas.coords(player), canvas.coords(pellet), canvas.coords(enemy1) )

playermoves()
pelletsscore()
damage()

window.bind("<s>",changeS)
window.bind("<w>",changeW)
window.bind("<d>",changeD)
window.bind("<a>",changeA)
window.bind("<u>",currentcords)

window.mainloop()