import tkinter as tk
from time import sleep
import keyboard
import threading
import datetime

class Entity:
    # General Entity Data
    speed = None
    name = None
    entity = None
    coordinates = (0, 0)

    def __init__(self, x: int, y: int, speed: int, name: str,entity: tk.Frame): # Entity constructor
        self.coordinates = (x, y)
        self.entity = entity
        self.speed = speed
        self.name = name

    def move(self, x, y): # Move function
        # Check if the entity is out of bounds
        if self.coordinates[0] + x * self.speed < 0 or self.coordinates[0] + x * self.speed > 750 or self.coordinates[1] + y * self.speed < 0 or self.coordinates[1] + y * self.speed > 550:
            return
        # Move the entity
        self.coordinates = (self.coordinates[0] + x * self.speed, self.coordinates[1] + y * self.speed)

    def render(self): # Renders the entity
        self.entity.place(x=self.coordinates[0], y=self.coordinates[1])

class Player(Entity): # Player class
    def __init__(self, x: int, y: int, name: str, entity: tk.Frame): # Player constructor
        super().__init__(x, y, 2.5, name, entity)

    def pulse(self, window: tk.Tk):
        self.entity.configure(width=60, height=60)
        self.coordinates = (self.coordinates[0] - 5, self.coordinates[1] - 5)
        window.configure(bg='blue')
        sleep(0.1)
        self.entity.configure(width=50, height=50)
        self.coordinates = (self.coordinates[0] + 5, self.coordinates[1] + 5)
        window.configure(bg='white')
        sleep(0.1)

def inputController(player: Player, window: tk.Tk, coords: tk.Label): # Input controller function to detect key presses
    print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Starting input controller") # Debugging
    while True: # Loop to detect key presses constantly
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

def ticker(coords: tk.Label, player: Player): # Ticker function to update the game
    print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Starting ticker controller")  # Debugging
    while True: # Loop to update the game constantly
        coords.configure(text=f'X: {player.coordinates[0]} Y: {player.coordinates[1]}')
        player.render()
        sleep(0.01667)

# Window
window = tk.Tk()
window.title('Game')
window.geometry('800x600')
window.resizable(False, False)
lbl = tk.Label(window, text='', font=('Arial Bold', 50))

# Entity starter
player = Player(0, 0, "Player",tk.Frame(window, width=50, height=50, bg='red'))

# Input controller
input = threading.Thread(target=inputController, args=(player, window, lbl))
input.start()

# Ticker
ticks = threading.Thread(target=ticker, args=(lbl, player))
ticks.start()

window.mainloop()