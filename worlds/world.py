import pygame

from ..camera import Camera
from ..game_object import GameObject


class World:
    def __init__(self):
        self.objects: list[GameObject] = []

    def add_object(self, obj: GameObject):
        self.objects.append(obj)

    def remove_object(self, obj: GameObject):
        if obj in self.objects:
            self.objects.remove(obj)

    def clear_objects(self):
        self.objects.clear()

    def get_objects(self):
        return self.objects

    def update(self, dt: float):
        for obj in self.objects:
            obj.update(dt)

    def draw(self, surface: pygame.Surface, camera: Camera):
        for obj in self.objects:
            obj.draw(surface, camera.offset, camera.rotation)
