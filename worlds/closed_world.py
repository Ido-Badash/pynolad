import pygame

from pynolad.camera import Camera
from pynolad.game_object import GameObject

from .world import World


class ClosedWorld(World):
    def __init__(
        self,
        width: int,
        height: int,
        objects: list[GameObject] = [],
        camera: Camera = None,
        camera_follow: bool = False,
    ):
        super().__init__(objects=objects, camera=camera)
        self.width = width
        self.height = height
        self.camera_follow = camera_follow

    def update(self, dt: float):
        for obj in self.objects:
            obj.update(dt)
            # Clamp objects inside world bounds
            obj.rect.clamp_ip(pygame.Rect(0, 0, self.width, self.height))
            self.camera.update(dt) if self.camera_follow else None
