from Entity import Entity
from math import atan
import tkinter as tk

class Bullet(Entity):
    Xmomentum = 0
    Ymomentum = 0

    def __init__(self, x: int, y: int, speed: float, damage: int, window: tk.Tk, target: tuple):
        super().__init__(x, y, speed, 5, "bullet", tk.Frame(window, width=5, height=5, bg="black"))
        self.speed = speed
        self.damage = damage
        self.__findMomentum(target)

    def __findMomentum(self, target: tuple):
        degrees = atan((self.coordinates[0] - target[0])/(self.coordinates[1] - target[1]))
        self.Xmomentum = self.speed * degrees
        self.Ymomentum = self.speed * (1 - degrees)
    def move(self) -> bool: # Moves the bullet and checks if it is out of bounds
        if self.coordinates[0] < 0 or self.coordinates[0] > 800 or self.coordinates[1] < 0 or self.coordinates[1] > 600:
            self.entity.destroy()
            return True

        self.coordinates = (self.coordinates[0] + self.Xmomentum, self.coordinates[1] + self.Ymomentum)
        self.updateColliders()
        self.render()

        return False



