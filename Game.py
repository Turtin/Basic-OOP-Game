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
    colliders = []
    size = 0

    def __init__(self, x: int, y: int, speed: float, size: int, name: str, entity: tk.Frame):  # Entity constructor
        self.coordinates = (x, y)
        self.entity = entity
        self.speed = speed
        self.name = name
        self.size = size

        print(
            f'{datetime.datetime.now().strftime('%H:%M:%S')}: Entity "{self.name}" created at {self.coordinates[0]}, {self.coordinates[1]} with a speed of {self.speed} and a size of {self.entity.winfo_width()}x{self.entity.winfo_height()}')  # Debugging

    def move(self, x, y):  # Move function
        # Check if the entity is out of bounds
        if (
                self.coordinates[0] + x * self.speed < 0 or
                self.coordinates[0] + x * self.speed > 750 or
                self.coordinates[1] + y * self.speed < 0 or
                self.coordinates[1] + y * self.speed > 550
        ): return

        # Move the entity
        self.coordinates = (self.coordinates[0] + x * self.speed, self.coordinates[1] + y * self.speed)

        # Update the colliders
        self.__updateColliders()

    def __updateColliders(self):
        self.colliders = {  # Updates the colliders by taking the coordinates and adding the size to them
            "nw": (self.coordinates[0], self.coordinates[1]),
            "n": (self.coordinates[0] + self.size / 2, self.coordinates[1]),
            "ne": (self.coordinates[0] + self.size, self.coordinates[1]),
            "sw": (self.coordinates[0], self.coordinates[1] + self.size),
            "s": (self.coordinates[0] + self.size / 2, self.coordinates[1] + self.size),
            "se": (self.coordinates[0] + self.size, self.coordinates[1] + self.size)
        }

    def checkCollision(self, entity) -> bool:  # Collision detection function
        for collider in entity.colliders:
            if (
                    self.colliders["nw"][0] < entity.colliders[collider][0] < self.colliders["ne"][0] and
                    self.colliders["nw"][1] < entity.colliders[collider][1] < self.colliders["sw"][1]
            ): return True
        return False

    def render(self):  # Renders the entity
        self.entity.place(x=self.coordinates[0], y=self.coordinates[1])


class Player(Entity):  # Player class
    def __init__(self):  # Player constructor
        super().__init__(0, 0, 2, 50, "Player", tk.Frame(window, width=50, height=50, bg='red'))

    def pulse(self, window: tk.Tk):
        self.entity.configure(width=60, height=60)
        self.coordinates = (self.coordinates[0] - 5, self.coordinates[1] - 5)
        window.configure(bg='blue')
        sleep(0.1)
        self.entity.configure(width=50, height=50)
        self.coordinates = (self.coordinates[0] + 5, self.coordinates[1] + 5)
        window.configure(bg='white')
        sleep(0.1)

    def detectDeath(self):
        for entity in Entities:
            if entity.name == "Player": continue
            if self.checkCollision(entity):
                print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Player died")
                return True
        return False


class Enemy(Entity):  # Enemy class
    def __init__(self, colour: str, name: str, speed: float, StartPos: (int, int)):  # Enemy constructor
        super().__init__(StartPos[0], StartPos[1], speed, 20, name, tk.Frame(window, width=20, height=20, bg=colour))

    def trackPlayer(self, player: Player): # Tracks the player
        if player.coordinates[0] + 15 > self.coordinates[0]:
            self.move(1, 0)
        if player.coordinates[0] + 15 < self.coordinates[0]:
            self.move(-1, 0)
        if player.coordinates[1] + 15 > self.coordinates[1]:
            self.move(0, 1)
        if player.coordinates[1] + 15 < self.coordinates[1]:
            self.move(0, -1)

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
    global Entities # Entities list
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
