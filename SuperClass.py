import tkinter as tk

class SpaceInvaderCanvas(tk.Canvas):
    def __init__(self, master=None, **attribut):
        super().__init__(master, **attribut)
        self.pack(fill="both", expand=True)

        self.master.title("Space Cookies")
        self.master.minsize(500,500)


class SpaceInvader():
    rootCanvas = SpaceInvaderCanvas(bg="black")

    def __init__(self):
        self.canvas = SpaceInvader.rootCanvas
        self.root_width = 0
        self.root_height = 0
        self.tac = 200

    def vw(self, x):
        return int(self.canvas.winfo_width()*x/100)

    def vh(self, y):
        return int(self.canvas.winfo_height()*y/100)

    def resize(self, event):
        #print(self.vw(100))
        pass