import tkinter as tk
from time import sleep
import keyboard
import threading

class Entity:
    speed = None
    entity = None

    def __init__(self, x: int, y: int, speed: int, entity: tk.Frame):
        self.x = x
        self.y = y
        self.entity = entity
        self.speed = 5

    def move(self, x, y):
        if self.x + x * self.speed < 0 or self.x + x * self.speed > 750 or self.y + y * self.speed < 0 or self.y + y * self.speed > 550:
            return
        self.x += x * self.speed
        self.y += y * self.speed
        self.render()

    def render(self):
        self.entity.place(x=self.x, y=self.y)

class Player(Entity):
    def __init__(self, x: int, y: int, entity: tk.Frame):
        super().__init__(x, y, 1, entity)

def inputController(player: Player, window: tk.Tk):
    print("started")
    while True:
        if keyboard.is_pressed('w'):
            player.move(0, -1*player.speed)
            sleep(0.01667)
        if keyboard.is_pressed('s'):
            player.move(0, 1*player.speed)
            sleep(0.01667)
        if keyboard.is_pressed('a'):
            player.move(-1*player.speed, 0)
            sleep(0.01667)
        if keyboard.is_pressed('d'):
            player.move(1*player.speed, 0)
            sleep(0.01667)
        if keyboard.is_pressed('e'):
            window.configure(bg='blue')
            sleep(0.01667)
            window.configure(bg='white')
        print(player.x, player.y)

window = tk.Tk()
window.title('Game')
window.geometry('800x600')
window.resizable(False, False)

player = Player(0, 0,tk.Frame(window, width=50, height=50, bg='red'))
input = threading.Thread(target=inputController, args=(player, window))
input.start()

window.mainloop()