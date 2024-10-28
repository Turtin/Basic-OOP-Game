from time import sleep
from entities import Player
import tkinter as tk
import datetime
import keyboard


def inputController(player: Player, window: tk.Tk, coords: tk.Label):  # Input controller function to detect key presses
    print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Starting input controller")  # Debugging
    while True:  # Loop to detect key presses constantly
        if window.focus_get() == None:
            continue

        if keyboard.is_pressed('w'):
            player.move(0, -1)
        if keyboard.is_pressed('s'):
            player.move(0, 1)
        if keyboard.is_pressed('a'):
            player.move(-1, 0)
        if keyboard.is_pressed('d'):
            player.move(1, 0)
        if keyboard.is_pressed('e'):
            player.pulse(window)
        if keyboard.is_pressed('f3'):
            coords.place(x=0, y=0, anchor='nw')
        if not keyboard.is_pressed('f3'):
            coords.place_forget()
        sleep(0.01667)