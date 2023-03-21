import tkinter as tk
from playsound import playsound
import time
from tkinter import *
import pyaudio


p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
if p.get_device_info_by_host_api_device_index(0, 1).get('name') == "iMac Speakers":
    print('Please use headphones :)')
    print('I think your peers are not interested in your reminder')
    exit()

def set_alarm():
    hr_c = ((int(h.get()) - int(time.strftime('%H'))) * 60) * 60
    mn_c = (int(m.get()) - int(time.strftime('%M'))) * 60
    alarm = h.get() + m.get()
    total = (hr_c + mn_c) - int(time.strftime('%S'))
    if (total < 0):
        total *= -1
    print(total)
    print(alarm)
    time.sleep(total)
    while True :
        current_time = time.strftime('%H%M')
        if (current_time == alarm):
            playsound('./sound.mp3')
            exit(0)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (200 // 2)
y = (screen_height // 2) - (100 // 2)
root.geometry(f"{200}x{100}+{x}+{y}")
root.title("Alarm 42")
root.resizable(False, False)
h = StringVar(root)
h.set(time.strftime('%H'))
m = StringVar(root)
m.set(time.strftime('%M'))
hours = Spinbox(root, from_=0, format='%02.0f',
                justify='center', to=23, width=3, textvariable=h).place(x=40, y=5)
minutes = Spinbox(root, from_=0, to=59, format='%02.0f',
                  justify='center', width=3, textvariable=m).place(x=110, y=5)
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.place(x=50, y=50)
root.mainloop()