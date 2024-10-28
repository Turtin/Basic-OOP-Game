from entities import Player, Enemy
from threads.GameTicker import ticker
from threads.InputController import inputController
import tkinter as tk
import threading

Entities = []  # List of entities

# Window
window = tk.Tk()
window.title('Game')
window.geometry('800x600')
window.resizable(False, False)
lbl = tk.Label(window, text='', font=('Arial Bold', 50))

# Entity starter
player = Player.Player(window, Entities)
enemy1 = Enemy.Zombie(window, "green", "bob", 1.5, (400, 300))
enemy2 = Enemy.Zombie(window, "green", "jerry", 1, (200, 100))
enemy3 = Enemy.Skeleton(window, "gray", "tom", 0.5, (600, 400), player)

Entities.append(enemy1)
Entities.append(enemy2)
Entities.append(enemy3)
Entities.append(player)

threads = []

# Input controller
input = threading.Thread(target=inputController, args=(player, window, lbl))
input.start()
threads.append(input)

# Ticker
ticks = threading.Thread(target=ticker, args=(window, Entities, lbl, player, threads))
ticks.start()

player.move(0, 0)

window.mainloop()
