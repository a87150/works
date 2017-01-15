from tkinter import *
from random import randint
mGui = Tk()
mGui.title('2048')
grid_text = [[StringVar() for i in range(4)] for j in range(4)]
grid = [[Label(width=10, height=5, textvariable=grid_text[i][j], font=("Helvetica", 16)).grid(row=i, column=j) for i in range(4)] for j in range(4)]
def place():
    global grid_text
    empty_spaces = []
    for i1, x in enumerate(grid_text):
        for i2, y in enumerate(x):
            if y.get() == '':
                empty_spaces.append(y)
    empty_spaces[randint(0, len(empty_spaces)-1)].set(str(2*randint(1, 2)))
def move(d):
    global grid_text
    cont = True
    while cont:
        cont = False
        for i1, x in list(enumerate(grid_text))[::-d[0] if d[0] else 1]:
            for i2, y in list(enumerate(x))[::-d[1] if d[1] else 1]:
                if y.get() != '':
                    if 0 <= i1+d[0] < 4 and 0 <= i2+d[1] < 4:
                        if grid_text[i1+d[0]][i2+d[1]].get() == y.get():
                            grid_text[i1+d[0]][i2+d[1]].set(str(int(y.get())*2))
                            y.set('')
                            cont = True
                        elif grid_text[i1+d[0]][i2+d[1]].get() == '':
                            grid_text[i1+d[0]][i2+d[1]].set(y.get())
                            y.set('')
                            cont = True
    place()
mGui.bind("<Left>", lambda a: move([0, -1]))
mGui.bind("<Up>", lambda a: move([-1, 0]))
mGui.bind("<Right>", lambda a: move([0, 1]))
mGui.bind("<Down>", lambda a: move([1, 0]))
place()
place()
mGui.mainloop()