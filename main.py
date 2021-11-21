import tkinter as tk 
import tkinter.ttk as ttk

import os as os

import SuperClass as sc
import Entity as e


""" os.system('xset r off') """

game = sc.SpaceInvader()
perso = e.Joueur()

sc.SpaceInvader.rootCanvas.master.mainloop()