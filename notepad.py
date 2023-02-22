import tkinter as tkr
from tkinter import filedialog
from tkinter import font
import os

win = tkr.Tk()
win.title('NOTEPAD')
win.geometry('700x600')
note_icon = tkr.PhotoImage(file=r'Notepad/notepad.png')
win.iconphoto(False, note_icon)

global opened_file
opened_file = False

global selected

frame = tkr.Frame(win)
frame.pack(padx=5,pady=5)

text_scroll = tkr.Scrollbar(frame)
text_scroll.pack(side=tkr.RIGHT, fill=tkr.Y)

# TEXT BOX
text = tkr.Text(frame, width=97, height=23, font=('Helvetica',16),selectbackground='black', selectforeground='white', undo=True, yscrollcommand=text_scroll.set)

text_scroll.config(command=text.yview())
text.pack()

# Menu
menu = tkr.Menu(win)
win.config(menu=menu)

# STATUS BAR
status_bar = tkr.Label(win, text='Ready      ', anchor=tkr.E)
status_bar.pack(fill=tkr.X,side=tkr.BOTTOM, ipady=7)


# Functions for the file menu
def new_file():
    try:
        text.delete('1.0',tkr.END)
        win.title('New File')
        status_bar.config(text='Ready      ')
        global opened_file
        opened_file = False
    except:
        return


# ICONS
new_icon = tkr.PhotoImage(file=r'Notepad/newfile.png')
open_icon = tkr.PhotoImage(file=r'Notepad/open.png')
save_icon = tkr.PhotoImage(file=r'Notepad/Save.png')
save_as_icon = tkr.PhotoImage(file=r'Notepad/save-as.png')
exit_icon = tkr.PhotoImage(file=r'Notepad/exit.png')
copy_icon = tkr.PhotoImage(file=r'Notepad/copy.png')
cut_icon = tkr.PhotoImage(file=r'Notepad/cut.png')
paste_icon = tkr.PhotoImage(file=r'Notepad/paste.png')
undo_icon = tkr.PhotoImage(file=r'Notepad/undo.png')
redo_icon = tkr.PhotoImage(file=r'Notepad/redo.png')


def open_file():
    try:
        text.delete('1.0',tkr.END)

        file_to_open = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open File',
                                                  filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'),
                                                             ('Python Files', '*.py'), ('All files', '*.*')))
        global opened_file
        opened_file = file_to_open

        for i in range(len(file_to_open)-1, 0, -1):
            if file_to_open[i] == '/':
                name = file_to_open[i+1:]
                win.title(name)
                break
        # status_bar.config(text=file_to_open)
        text_file = open(file_to_open, 'r')
        stuff = text_file.read()
        text.insert(tkr.END, stuff)

    except:
        return


def save_as_file():
    try:
        text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir=os.getcwd(),title='Save File',
                                                 filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'),
                                                            ('Python Files', '*.py'), ('All Files', '*.*')))
        global opened_file
        opened_file = text_file
        for i in range(len(text_file)-1, 0, -1):
            if text_file[i] == '/':
                name = text_file[i+1:]
                win.title(name)
                break

        if text_file:
            text_file = open(text_file, 'w')
            text_file.write(text.get(1.0, tkr.END))
    except:
        return


def save_file():
    try:
        global opened_file
        if opened_file:
            text_file = open(opened_file, 'w')
            text_file.write(text.get(1.0, tkr.END))
        else:
            save_as_file()
    except:
        return


# FILE MENU
file_menu = tkr.Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', image=new_icon, compound=tkr.LEFT, command=new_file)
file_menu.add_command(label='Open', image=open_icon, compound=tkr.LEFT, command=open_file)
file_menu.add_command(label='Save As', image=save_as_icon, compound=tkr.LEFT, command=save_as_file)
file_menu.add_command(label='Save', image=save_icon, compound=tkr.LEFT, command=save_file)
file_menu.add_command(label='Exit', image=exit_icon, compound=tkr.LEFT, command=win.quit)


# Functions for edit menu
def copy():
    global selected
    if text.selection_get():
        selected = text.selection_get()
        win.clipboard_clear()

def cut():
    global selected
    if text.selection_get():
        selected = text.selection_get()
        text.delete('sel.first', 'sel.last')


def paste():
    global selected
    if selected:
        pos = text.index(tkr.INSERT)
        text.insert(pos, selected)


# EDIT MENU
edit_menu = tkr.Menu(menu, tearoff=False)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', image=copy_icon, compound=tkr.LEFT, command=copy)
edit_menu.add_command(label='Cut', image=cut_icon, compound=tkr.LEFT, command=cut)
edit_menu.add_command(label='Paste', image=paste_icon, compound=tkr.LEFT, command=paste)
edit_menu.add_command(label='Undo', image=undo_icon, compound=tkr.LEFT, command=text.edit_undo)
edit_menu.add_command(label='Redo', image=redo_icon, compound=tkr.LEFT, command=text.edit_redo)


win.mainloop()
