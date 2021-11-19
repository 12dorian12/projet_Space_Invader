import tkinter as tk 
import tkinter.ttk as ttk

import SuperClass as sc
import Entity as e


game = sc.SpaceInvader()
perso = e.Entity()
perso.binding()

sc.SpaceInvader.canvas.mainloop()