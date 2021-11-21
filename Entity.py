import SuperClass as sc
import tkinter as tk
from PIL import Image,ImageTk

class Entity(sc.SpaceInvader):
    def __init__(self):
        sc.SpaceInvader.__init__(self)
        self.canvas.bind("<Configure>", self.update)

        self.vie = 1
        self.sprite = Image.open("media/image/male_sprite_model.png")
        self.anim = [[2,3,4,3,2,1,0,1], [2,3,4,3,2,1,0,1], [1,2,3,5,6,7], [1,2,3,5,6,7]]
        self.direction = 1
        self.animation = 0
        self.cropingSrpite() #definie self.cropSprite
        self.position = (10, 10)
        self.canvas.after(self.tac, self.tic)

    def cropingSrpite(self, direction = None, animation = None):#haut direction 0,   bas direction 1,   droite direction 2,   gauche direction 3
        if direction == None:
            direction = self.direction
        else:
            self.direction = direction

        if animation == None:
            animation = self.animation
        else:
            self.animation = animation
        self.cropSprite = self.sprite.crop((32*self.anim[direction][animation], 64*direction, 32*(self.anim[direction][animation]+1), 64*(direction+1)))
        self.update()
        
    def update(self, e=None):
        #self.canvas.delete("all") 
        """
        redimentionne l'image
        """
        #resize
        self.resizeSprite= self.cropSprite.resize((self.vw(10)+1,2*self.vw(10)+1), Image.ANTIALIAS)#+1 car on ne doit pas resize par 0
        self.tkResizeSprite = ImageTk.PhotoImage(self.resizeSprite)
        self.canvas.create_image(self.vw(50),self.vh(50), image = self.tkResizeSprite)
        

    def tic(self):
        if self.animation+1 < len(self.anim[self.direction]):
            self.animation += 1
        else:
            self.animation = 0
        self.canvas.after(self.tac, self.tic)
        self.cropingSrpite()
        
class Joueur(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.canvas.bind_all("<Key>", self.moving)
    
    def moving(self, e):
        if e.char == "z":
            self.cropingSrpite(0,0)
        elif e.char == "s":
            self.cropingSrpite(1,0)
        elif e.char == "d":
            self.cropingSrpite(2,0)
        elif e.char == "q":
            self.cropingSrpite(3,0)
        else:
            print(e.char)
