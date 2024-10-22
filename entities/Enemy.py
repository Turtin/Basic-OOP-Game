from Entity import Entity
from Player import Player
import tkinter as tk

class Enemy(Entity):  # Enemy class
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