from Entity import Entity
from entities import Player
from entities.weapons.Bullet import Bullet
import tkinter as tk
import random

class Zombie(Entity):  # Enemy class
    def __init__(self, window: tk.Tk, colour: str, name: str, speed: float, StartPos: (int, int)):  # Enemy constructor
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

class Skeleton(Entity):
    activeBullets = []
    player = None
    window = None

    def __init__(self, window: tk.Tk, colour: str, name: str, speed: float, StartPos: (int, int), player: Player):  # Enemy constructor
        super().__init__(StartPos[0], StartPos[1], speed, 20, name, tk.Frame(window, width=20, height=20, bg=colour))
        self.player = player
        self.window = window

    def trackPlayer(self, player: Player): # Tracks the player
        self.handleBullets()

        if player.coordinates[0] + 15 > self.coordinates[0]:
            self.move(1, 0)
        if player.coordinates[0] + 15 < self.coordinates[0]:
            self.move(-1, 0)
        if player.coordinates[1] + 15 > self.coordinates[1]:
            self.move(0, 1)
        if player.coordinates[1] + 15 < self.coordinates[1]:
            self.move(0, -1)

        if random.randint(0, 100) == 1:
            self.shoot(player)

    def shoot(self, player: Player):
        bullet = Bullet(self.coordinates[0] + self.size/2, self.coordinates[1] + self.size/2, 5, 10, self.window, self.player.coordinates)
        self.activeBullets.append(bullet)

    def handleBullets(self):
        for bullet in self.activeBullets:
            if bullet.move(): # If the bullet is out of bounds
                self.activeBullets.remove(bullet) # Remove the bullet from the list