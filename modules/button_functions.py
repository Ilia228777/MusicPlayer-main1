import customtkinter as ctk
import modules.data as m_data
import modules.json_operation as m_jorge
import modules.screen_app as m_app
import pygame as pg
import tkinter as tk
import random 

pg.mixer.init()
pg.init()
paused = False

def mix():
    random.shuffle(m_data.list_music)
    m_app.main_app.LIST_BOX.delete(first = 0, last = ctk.END)
    for song in m_data.list_music:
        m_app.main_app.LIST_BOX.insert(ctk.END, song)

    m_data.data = {
        "music": m_data.list_music,
        "volume": m_data.volume
    }
    m_jorge.write_json()


def delete():
    song_tam = m_app.main_app.LIST_BOX.curselection()
    current_index = m_app.main_app.LIST_BOX.index(song_tam)
    m_app.main_app.LIST_BOX.delete(first = current_index, last = None)
    pg.mixer.music.stop()
    del m_data.list_music[current_index]
    m_data.data = {
        "music": m_data.list_music,
        "volume": m_data.volume
    }
    m_jorge.write_json()

def stop():
    pg.mixer.music.stop()

def pause():
    global paused
    
    if paused == False:
        pg.mixer.music.pause()
        paused = True

    else:
        pg.mixer.music.unpause()
        pg.mixer.music.set_endevent(m_app.main_app.SONG_END)
        paused = False

def previous_track():
    pos = pg.mixer.music.get_pos()
    if pos > 5000:
        pg.mixer.music.play()
        pg.mixer.music.set_endevent(m_app.main_app.SONG_END)
        m_app.main_app.MUSIC_NAME.place_forget()
        m_app.main_app.MUSIC_NAME = ctk.CTkLabel(master= m_app.main_app, text= m_app.main_app.LIST_BOX.get(tk.ACTIVE).split("/")[-1]) # self.LIST_BOX
        m_app.main_app.MUSIC_NAME.place(x = 310,y = 15)
        
    else:
        try:
            previous = m_app.main_app.LIST_BOX.curselection()
            previous = previous[0]-1
            song = m_app.main_app.LIST_BOX.get(previous)
            pg.mixer.music.load(song)   
            pg.mixer.music.play()
            pg.mixer.music.set_endevent(m_app.main_app.SONG_END)
            m_app.main_app.LIST_BOX.selection_clear(0, ctk.END)
            m_app.main_app.LIST_BOX.activate(previous)
            m_app.main_app.LIST_BOX.selection_set(previous)
            m_app.main_app.MUSIC_NAME.place_forget()
            m_app.main_app.MUSIC_NAME = ctk.CTkLabel(master= m_app.main_app, text= m_app.main_app.LIST_BOX.get(tk.ACTIVE).split("/")[-1]) # self.LIST_BOX
            m_app.main_app.MUSIC_NAME.place(x = 310,y = 15)
            
        except: 
            pg.mixer.music.play()
            pg.mixer.music.set_endevent(m_app.main_app.SONG_END)
        

def next_track():
    try:
        next = m_app.main_app.LIST_BOX.curselection()
        next = next[0]+1
        song = m_app.main_app.LIST_BOX.get(next)
        pg.mixer.music.load(song)   
        pg.mixer.music.play()
        pg.mixer.music.set_endevent(m_app.main_app.SONG_END)
        m_app.main_app.LIST_BOX.selection_clear(0, ctk.END)
        m_app.main_app.LIST_BOX.activate(next)
        m_app.main_app.LIST_BOX.selection_set(next)
        m_app.main_app.MUSIC_NAME.place_forget()
        m_app.main_app.MUSIC_NAME = ctk.CTkLabel(master= m_app.main_app, text= m_app.main_app.LIST_BOX.get(tk.ACTIVE).split("/")[-1]) # self.LIST_BOX
        m_app.main_app.MUSIC_NAME.place(x = 310,y = 15)
    except:
        pass

def volume_add():
    if m_data.volume < 1:
        m_data.volume += 0.1
        m_data.data = {
            "music": m_data.list_music,
            "volume": m_data.volume
        }
        m_jorge.write_json()
        pg.mixer.music.set_volume(m_data.volume)
        
def volume_minus():
    if m_data.volume >= 0.1:
        m_data.volume -= 0.1
        m_data.data = {
            "music": m_data.list_music,
            "volume": m_data.volume
        }
        m_jorge.write_json()
        pg.mixer.music.set_volume(m_data.volume)

def add_song():
    filename = ctk.filedialog.askopenfilename(
        filetypes = (("mp3 Music Files", "*.mp3"),
                   ("m4a Music Files", "*.m4a"), 
                   ("ogg Music Files","*.ogg"), 
                   ("wav Music Files","*.wav"))
    )
    m_data.list_music.append(filename)
    m_data.data = {
        "music": m_data.list_music,
        "volume": m_data.volume
    }
    m_jorge.write_json()
    filename_splitted = filename.split("/")
    m_app.main_app.LIST_BOX.insert(ctk.END, filename)

def playsong():
    sound = m_app.main_app.LIST_BOX.get(tk.ACTIVE)
    # next_sound = m_app.main_app.LIST_BOX.get(m_app.main_app.LIST_BOX.index(tk.ACTIVE)+1) # vot eto vot pishi
    pg.mixer.music.load(sound)
    pg.mixer.music.play()
    # pg.mixer.music.queue(next_sound) # вот ета упери
    pg.mixer.music.set_endevent(m_app.main_app.SONG_END)
    m_app.main_app.MUSIC_NAME.place_forget()
    m_app.main_app.MUSIC_NAME = ctk.CTkLabel(master= m_app.main_app, text= m_app.main_app.LIST_BOX.get(tk.ACTIVE).split("/")[-1]) # self.LIST_BOX
    m_app.main_app.MUSIC_NAME.place(x = 310,y = 15)