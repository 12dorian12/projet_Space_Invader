import tkinter as tk

class SpaceInvaderCanvas(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand="yes")

        self.master.title("Space Cookies")
        self.master.minsize(300,300)


class SpaceInvader():
    canvas = SpaceInvaderCanvas()

    def __init__(self):
        self.root_width = 0
        self.root_height = 0

    def vw(self, x):
        return int(SpaceInvader.canvas.winfo_width()*x/100)

    def vh(self, y):
        return int(SpaceInvader.canvas.winfo_height()*y/100)

    def binding(self):
        SpaceInvader.canvas.bind("<Configure>", self.resize)

    def resize(self, event):
        #print(self.vw(100))
        pass