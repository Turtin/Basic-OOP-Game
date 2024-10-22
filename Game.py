import tkinter as tk
from time import sleep
import keyboard
import threading
import datetime

def endGame():
    global window
    loose = tk.Label(window, text='You lost!', font=('Arial Bold', 50)) # Creates a label that says "You lost!"
    quit = tk.Button(window, text='Quit', font=('Arial Bold', 30), command=lambda: [
        window.destroy(),
        ticks.join(),
        input.join(),
        exit(0)
    ]) # Creates a button that quits the game

    quit.place(x=400, y=400, anchor='center') # Places the button in the center of the screen
    loose.place(x=400, y=300, anchor='center') # Places the label in the center of the screen

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


def ticker(coords: tk.Label, player: Player):  # Ticker function to update the game
    print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Starting ticker controller")  # Debugging
    global Entities # Entities listas
    while True:  # Loop to update the game constantly
        if window.focus_get() == None:  # Pauses the game when out of focus
            continue

        coords.configure(text=f'X: {player.coordinates[0]} Y: {player.coordinates[1]}')
        for entity in Entities: # Loops through all entities and renders them
            entity.render() # Renders the entity
            if not entity.name == "Player":
                entity.trackPlayer(player) # Tracks the player

        if player.detectDeath(): # Checks if the player has died
            endGame()
            break

        sleep(0.01667)  # Sleeps for 1/60th of a second

Entities = []  # List of entities

# Window
window = tk.Tk()
window.title('Game')
window.geometry('800x600')
window.resizable(False, False)
lbl = tk.Label(window, text='', font=('Arial Bold', 50))

# Entity starter
player = Player()
enemy1 = Enemy("green", "bob", 1.5, (400, 300))
enemy2 = Enemy("green", "jerry", 1, (200, 100))
enemy3 = Enemy("green", "tom", 0.5, (600, 400))

Entities.append(enemy1)
Entities.append(enemy2)
Entities.append(enemy3)
Entities.append(player)

# Input controller
input = threading.Thread(target=inputController, args=(player, window, lbl))
input.start()

# Ticker
ticks = threading.Thread(target=ticker, args=(lbl, player))
ticks.start()

player.move(0, 0)

window.mainloop()
