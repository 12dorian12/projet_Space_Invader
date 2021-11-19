import SuperClass as sc
import tkinter as tk
from PIL import Image,ImageTk

class Entity(sc.SpaceInvader):
    def __init__(self):
        sc.SpaceInvader.__init__(self)

        self.vie = 1
        self.spriteSheet = "media/image/male_sprite_model.png"
        self.img0 = tk.PhotoImage(file=self.spriteSheet)

        sc.SpaceInvader.canvas.create_image(0,0, image = self.img0)

    def resize(self, event):
        
        self.img = (Image.open(self.spriteSheet))
        self.resized_image= self.img.resize((32*self.vw(1),64*self.vw(1)), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)

        sc.SpaceInvader.canvas.create_image(10,10, image = self.img0)

        
        print(self.vw(100))