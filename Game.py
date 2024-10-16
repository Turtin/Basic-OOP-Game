import tkinter as tk
from time import sleep
import keyboard
import threading

class Entity:
    speed = 10
    entity = None

    def __init__(self, x: int, y: int, entity: tk.Frame):
        self.x = x
        self.y = y
        self.entity = entity

    def move(self, x, y):
        self.x += x * self.speed
        self.y += y * self.speed
        self.render()

    def render(self):
        self.entity.place(x=self.x, y=self.y)

class Player(Entity):
    speed = 1

def inputController(player: Player):
    print("started")
    while True:
        if keyboard.is_pressed('w'):
            player.move(0, -1)
            sleep(0.1)
        if keyboard.is_pressed('s'):
            player.move(0, 1)
            sleep(0.1)
        if keyboard.is_pressed('a'):
            player.move(-1, 0)
            sleep(0.1)
        if keyboard.is_pressed('d'):
            player.move(1, 0)
            sleep(0.1)
        print(player.x, player.y)

window = tk.Tk()
window.title('Game')
window.geometry('800x600')
window.resizable(False, False)

player = Entity(0, 0, tk.Frame(window, width=50, height=50, bg='red'))
input = threading.Thread(target=inputController, args=(player,))
input.start()

window.mainloop()