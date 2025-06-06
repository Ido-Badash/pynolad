import pygame

from ..camera import Camera
from ..game_object import GameObject


class World:
    def __init__(self, objects: list[GameObject] = [], camera: Camera = None):
        self.objects = objects
        self.camera = camera if camera is not None else Camera(800, 600)

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
        if self.camera:
            self.camera.update(dt)
        for obj in self.objects:
            obj.update(dt)

    def draw(self, surface: pygame.Surface):
        for obj in self.objects:
            obj.draw(surface, self.camera.offset, self.camera.rotation)

    def get_camera(self):
        return self.camera

    def set_camera(self, camera: Camera):
        self.camera = camera
