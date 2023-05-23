import customtkinter as ctk
import tkinter as tk 
import pygame as pg
pg.init()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.APP_WIDTH = 500
        self.APP_HEIGHT = 500
        self.title("PadSound")
        self.SONG_END = pg.USEREVENT + 1
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{100}+{100}")
        self.resizable(False, False)
        self.LIST_BOX = tk.Listbox(master= self, 
                                   selectmode= tk.SINGLE, 
                                   width = 33,
                                   height= 25,
                                   bg= "#282828",
                                   font = ("Calibri", 10),
                                   fg = "white",
                                   selectbackground = "gray",
                                   activestyle = "none",
                                   selectforeground = "black")# дима черный
            
        self.MUSIC_NAME = ctk.CTkLabel(master= self, text= self.LIST_BOX.get(tk.ACTIVE)) # self.LIST_BOX
        self.MUSIC_NAME.place(x = 325,y = 20)#это всё скобки, они нам код сломали
        self.LIST_BOX.place(x=20 , y=20)# ААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА ДИМА ОТВЕТИЛ
        self.SCROLLBAR = ctk.CTkScrollbar(master=self, height = 403, bg_color= "gray", button_color="white", button_hover_color= "lightgray") # Ms. White
        self.SCROLLBAR.place(x = 254, y = 21)
        self.LIST_BOX.config(yscrollcommand= self.SCROLLBAR.set)
        self.SCROLLBAR.configure(command=self.LIST_BOX.yview)


main_app = App()

         