from tkinter import *
import pygame
from tkinter import filedialog
import os
import time
from mutagen.mp3 import MP3

win = Tk()

win.title('MUSIC PLAYER')
win.geometry('600x400')
music_icon = PhotoImage(file=r'musicplayer/icon.png')
win.iconphoto(False, music_icon)

pygame.mixer.init()


def play_time():
    try:
        current_time = pygame.mixer.music.get_pos()//1000

        convert_time = time.strftime('%M:%S', time.gmtime(current_time))

        song_current = song_box.curselection()[0]
        song_current = song_dict[song_box.get(song_current)]
        song_mut = MP3(song_current)
        song_length = song_mut.info.length
        convert_song_length = time.strftime('%M:%S', time.gmtime(song_length))

        status_bar.config(text='Time Elapsed:' + ' ' + convert_time + ' ' + 'of' + ' ' + convert_song_length)
        status_bar.after(1000, play_time)

    except:
        return


# Define SongBox
song_box = Listbox(win, bg='black', fg='green', width=80, height=16, selectbackground='grey', selectforeground='cyan')
song_box.pack(pady=20)

# Define Button
back_button_icon = PhotoImage(file=r'musicplayer/rewind-symbol.png')

play_button_icon = PhotoImage(file=r'musicplayer/video-player.png')
forward_button_icon = PhotoImage(file=r'musicplayer/fast-forward-media-control-button.png')
pause_button_icon = PhotoImage(file=r'musicplayer/pause-button.png')
stop_button_icon = PhotoImage(file=r'musicplayer/stop.png')

# Create Player COntrol Frame
controls_frame = Frame(win)
controls_frame.pack()


# Creating Functions for the buttons
def play_song():
    try:
        song = song_box.get(ACTIVE)
        pygame.mixer.music.load(song_dict[song])
        pygame.mixer.music.play(loops=0)
        play_time()

    except:
        return


def stop_song():
    try:
        pygame.mixer.music.stop()
        song_box.selection_clear(ACTIVE)

    except:
        return
    # Clear Status Bar
    status_bar.config(text='')


paused = False


def pause_song():
    global paused
    try:
        if not paused:
            pygame.mixer.music.pause()
            paused = True
        else:
            pygame.mixer.music.unpause()
            paused = False


    except:
        return


def next_song():
    try:
        playing = song_box.curselection()[0]
        next_one = playing + 1
        song_to_play = song_dict[song_box.get(next_one)]
        pygame.mixer.music.load(song_to_play)
        pygame.mixer.music.play(-1)

        # selecting the new next song
        song_box.selection_clear(0, END)
        song_box.activate(next_one)
        song_box.selection_set(next_one)

    except:
        return

def previous_song():
    try:
        playing = song_box.curselection()[0]
        next_one = playing - 1
        song_to_play = song_dict[song_box.get(next_one)]
        pygame.mixer.music.load(song_to_play)
        pygame.mixer.music.play(-1)

        # selecting the new next song
        song_box.selection_clear(0, END)
        song_box.activate(next_one)
        song_box.selection_set(next_one)

    except:
        return


# Create Player Control Button
back_button = Button(controls_frame, image=back_button_icon, borderwidth=0, command=previous_song)
play_button = Button(controls_frame, image=play_button_icon, borderwidth=0, command=play_song)
stop_button = Button(controls_frame, image=stop_button_icon, borderwidth=0, command=stop_song)
pause_button = Button(controls_frame, image=pause_button_icon, borderwidth=0, command=pause_song)
forward_button = Button(controls_frame, image=forward_button_icon, borderwidth=0, command=next_song)


back_button.grid(row=0, column=1, padx=20)
pause_button.grid(row=0, column=2, padx=20)
play_button.grid(row=0, column=3, padx=20)
stop_button.grid(row=0, column=4, padx=20)
forward_button.grid(row=0, column=5, padx=20)

song_dict = {}

# Create Menu
menu = Menu(win)
win.config(menu=menu)


# Add Song Menu
def add_song():
    song = filedialog.askopenfilename(initialdir=os.getcwd(), title='Choose the song', filetypes=(('mp3 Files', '*.mp3'),))

    for i in range(len(song)-1, -1, -1):
        if song[i] == '/':
            song1 = song[i+1:]
            break
    song_dict[song1] = song
    # Add Song to ListBox
    song_box.insert(END, song1)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir=os.getcwd(), title='Choose the song',
                                      filetypes=(('mp3 Files', '*.mp3'),
                                                 ('wav Files', '*.wav')))
    # Looping through selected files
    for song in songs:
        for i in range(len(song) - 1, -1, -1):
            if song[i] == '/':
                song2 = song[i + 1:]
                break

        song_dict[song2] = song
        song_box.insert(END, song2)


add_Song_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='Add Songs', menu=add_Song_menu)
add_Song_menu.add_command(label='Add One Song', command=add_song)
add_Song_menu.add_command(label='Add Number of songs', command=add_many_songs)


def delete_song():
    del song_dict[song_box.get(ACTIVE)]
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()
    print(song_dict)


def delete_all_song():
    song_box.delete(0, END)
    pygame.mixer.music.stop()
    song_dict.clear


# status bar
status_bar = Label(win, text='Current Time:', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(side=BOTTOM, fill=X, ipady=2)


delete_song_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='Remove Songs', menu=delete_song_menu)
delete_song_menu.add_command(label='Delete A Song from playlist', command=delete_song)
delete_song_menu.add_command(label='Delete All Songs from playlist', command=delete_all_song)

win.mainloop()

pygame.mixer.music.stop()
