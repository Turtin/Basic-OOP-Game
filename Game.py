import tkinter as tk
import keyboard

class Entity:
    speed = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x * self.speed
        self.y += y * self.speed

        print(f'x: {self.x}, y: {self.y}')

class Player(Entity):
    speed = 1

window = tk.Tk()