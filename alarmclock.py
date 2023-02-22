from tkinter import *
import pygame
import time
import datetime
from tkinter import ttk
from threading import Thread

win = Tk()
win.title('ALARM CLOCK')
win.geometry('300x250')
win.wm_resizable(False,False)
win.config(bg='black')
iconphoto = PhotoImage(file=r'Alarm/clocks.png')
win.iconphoto(False, iconphoto)
pygame.mixer.init()

hour = time.strftime('%H')
minute = time.strftime('%M')
seconds = time.strftime('%S')


def current_time():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    seconds = time.strftime('%S')
    current_time_label.config(text=hour + ':' + minute + ':' + seconds)

    current_time_label.after(1000, current_time)


timeLabel = Label(win, text='Time:', font=('Helvetica', 14), bg='black', fg='white')
timeLabel.place(x=145,y=10)


current_time_label = Label(win, text='', font=('Helvetica', 14), bg='black', fg='white')
current_time_label.place(x=200,y=10)


current_time()


def alarm_starter():
    a = Thread(target = alarm)
    a.start()


def alarm():
    if c1.get() == 'PM' and int(e_hr.get()) < 12:
        alarm_hr = int(e_hr.get()) + 12
    else:
        alarm_hr = int(e_hr.get())
    alarm_min = int(e_min.get())
    alarm_sec = int(e_sec.get())
    varstring.set("alarm set!")
    while True:
        if alarm_hr == datetime.datetime.now().hour and alarm_min == datetime.datetime.now().minute and\
                alarm_sec == datetime.datetime.now().second:
            pygame.mixer.music.load(r'Alarm/alarm_clock_10.mp3')
            pygame.mixer.music.play(1)
            break


labelFont = ("Helvetica",14,"bold")

hour_label = Label(win, text='Hours:', bg='black', fg='yellow',font=labelFont)
hour_label.place(x=20,y=50)

min_label = Label(win, text='Minutes:', bg='black', fg='yellow',font=labelFont)
min_label.place(x=20,y=90)

sec_label = Label(win, text='Seconds:', bg='black', fg='yellow',font=labelFont)
sec_label.place(x=20,y=130)

e_hr = Entry(win)
e_hr.config(bg='white', fg='black',font=labelFont, width=12)
e_hr.place(x=145,y=50)

e_min = Entry(win)
e_min.config(bg='white', fg='black',font=labelFont, width=12)
e_min.place(x=145,y=90)

e_sec = Entry(win)
e_sec.config(bg='white', fg='black',font=labelFont, width=12)
e_sec.place(x=145,y=130)


btn = Button(win, text='Set Alarm', command=alarm_starter)
btn.config(bg='white', fg='black')
btn.place(x=110,y=200)

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'fieldbackground': 'black',
                                       'background': 'white',
                                       'foreground': 'black'
                                       }}})

combostyle.theme_use('combostyle')

# AM/PM
am_pm = Label(win, text='AM/PM', fg='yellow', bg='black',font=labelFont)
am_pm.place(x=20,y=170)
c1 = ttk.Combobox(win, values=['AM', 'PM'],font=labelFont,width=11)
c1['state'] = 'readonly'
c1.place(x=145,y=170)

varstring = StringVar()
varstring.set("")
success = Label(win,textvariable=varstring,background="black",foreground="green",font=("Helvetica",15))
success.place(x=30,y=10)

win.mainloop()
