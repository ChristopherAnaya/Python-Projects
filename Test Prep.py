import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Draw an "X" by creating two diagonal lines
canvas.create_line(20, 20, 120, 120, fill="black", width=5)  # First diagonal
canvas.create_line(120, 20, 20, 120, fill="black", width=5)  # Second diagonal

root.mainloop()