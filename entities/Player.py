from entities.Enemy import Skeleton
from Entity import Entity
from time import sleep
import tkinter as tk
import datetime


class Player(Entity):  # Player class
    entities = []

    def __init__(self, window: tk.Tk, entities: list):  # Player constructor
        super().__init__(0, 0, 2, 50, "Player", tk.Frame(window, width=50, height=50, bg='red'))
        self.entities = entities

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
        global  entities
        for entity in self.entities:
            if isinstance(entity, Player): continue  # Skip the player

            if self.checkCollision(entity): # If the player collides with an entity
                print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Player died")
                return True

            if isinstance(entity, Skeleton):
                for bullet in entity.activeBullets:
                    if self.checkCollision(bullet):
                        print(f"{datetime.datetime.now().strftime('%H:%M:%S')}: Player died")
                        return True
        return False
