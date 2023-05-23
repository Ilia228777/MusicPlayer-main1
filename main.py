import modules.screen_app as m_app
import modules.button
import modules.button_functions as bt
import pygame as pg
import modules.data as datatatatatata
import customtkinter as ctk

def run():
    running = True
    for el in datatatatatata.data["music"]:
        m_app.main_app.LIST_BOX.insert(ctk.END, el)
    while running:
        for event in pg.event.get():
            if event.type == m_app.main_app.SONG_END:
                if not m_app.main_app.STOPPED:
                    bt.next_track()
        m_app.main_app.update_idletasks()
        m_app.main_app.update()

run()

