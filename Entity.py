import datetime
import tkinter as tk

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
        self.updateColliders()

    def updateColliders(self):
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

