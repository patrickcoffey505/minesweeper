import tkinter as tk

import random

class Minesweeper:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("mine sweeper")

        self.user = tk.StringVar()
        self.user.set("30")

        self.define_widgets()

        self.mines = random.sample([ (i,j) for i in range(25) for j in range(50) ], 30)
        self.marks = []

        print(self.mines)
        self.main.mainloop()
        

    def define_widgets(self):
        self.canvas = tk.Canvas(self.main, width = 1010, height = 505,
                                bg="#f3f3f3")
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.boxes=[ [ ] for i in range(25)]
        self.texts=[ [ ] for i in range(25)]
        for i in range(25):
            for j in range(50):
                box = self.canvas.create_rectangle(3+j*20, 3+i*20, 20+j*20, 20+i*20)
                self.boxes[i].append(box)
        for i in range(25):
            for j in range(50):
                text = self.canvas.create_text(11+j*20, 11+i*20, text="?", width=8)
                self.texts[i].append(text)
        self.canvas.bind('<Button-1>', self.handler)
        self.canvas.bind('<Button-3>',self.marked)
        self.reset = tk.Button(self.main, text = 'RESET', command = self.resetAll)
        self.reset.grid(row = 1, column = 0)
        self.label = tk.Label(self.main, text = "# OF MINES: ")
        self.label.grid(row = 1, column = 1, sticky= 'E')
        self.entry = tk.Entry(self.main, textvariable = self.user)
        self.entry.grid(row = 1, column = 2, sticky = 'W')
    

    def handler(self, event):
        row = (event.y-2)//20
        column = (event.x-2)//20
        if (row, column) in self.mines:
            self.canvas.create_text(500,250, text= "Boom", font = ("Helvetica", 30))
        self.canvas.delete(self.boxes[row][column])
        self.canvas.itemconfig(self.texts[row][column], text=str(self.nr_mines(row, column)), fill = "blue") 

    def marked(self, event):
        row = (event.y-2)//20
        column = (event.x-2)//20
        if (row, column) in self.marks:
            self.canvas.itemconfig(self.texts[row][column], text = '?', fill = 'black')
            self.marks.remove((row, column))
        else:
            self.canvas.itemconfig(self.texts[row][column], text = 'X', fill = 'red')
            self.marks.append((row,column))

    def neighboring(ii, jj):
        """returns a list of all neighboring cells"""
        maxrow, maxcol = 50, 25
        return[ (i, j) for i in range(ii-1,ii+2) for j in range(jj-1, jj+2) if i >= 0 and 
                i < maxrow and j>=0 and j< maxcol and not (i==ii and j==jj) ]

    def nr_mines(self, row, column):
        count = 0
        for field in Minesweeper.neighboring(row, column):
            if field in self.mines:
                count += 1
        if (row, column) in self.mines:
            count += 1
        return count

    def resetAll(self):
        mineNum = self.entry.get()
        self.main.destroy()

        self.main = tk.Tk()
        self.main.title("mine sweeper")

        self.user = tk.StringVar()
        self.user.set(mineNum)

        self.define_widgets()

        self.mines = random.sample([ (i,j) for i in range(25) for j in range(50) ], int(mineNum))

        print(self.mines)
        self.main.mainloop()

ms = Minesweeper()
