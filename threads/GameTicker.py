from entities import Player
from time import sleep
import tkinter as tk
import datetime
import threading

runningThreads = []

def __closeThreads():
    global runningThreads
    for thread in runningThreads:
        thread.join()
    threading.main_thread().join()
    exit()

def endGame(window: tk.Tk):  # Function to end the game

    lose = tk.Label(window, text='You lost!', font=('Arial Bold', 50)) # Creates a label that says "You lost!"
    quit = tk.Button(window, text='Quit', font=('Arial Bold', 30), command=lambda: [
        print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Ending game"),  # Debugging
        window.destroy(),
        __closeThreads(),
    ]) # Creates a button that quits the game

    quit.place(x=400, y=400, anchor='center') # Places the button in the center of the screen
    lose.place(x=400, y=300, anchor='center') # Places the label in the center of the screen


def ticker(window: tk.Tk, entities: list, coords: tk.Label, player: Player, threads):  # Ticker function to update the game
    print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Starting game ticker")  # Debugging
    global runningThreads
    runningThreads = threads
    while True:  # Loop to update the game constantly
        if window.focus_get() == None:  # Pauses the game when out of focus
            continue

        coords.configure(text=f'X: {player.coordinates[0]} Y: {player.coordinates[1]}')
        for entity in entities: # Loops through all entities and renders them
            entity.render() # Renders the entity
            if not entity.name == "Player":
                entity.trackPlayer(player) # Tracks the player

        if player.detectDeath(): # Checks if the player has died
            endGame(window)
            break

        sleep(0.01667)  # Sleeps for 1/60th of a second