import pygame

from pynolad.camera import Camera
from pynolad.game_object import GameObject

from .closed_world import ClosedWorld


class GravitedClosedWorld(ClosedWorld):
    def __init__(self, *args, strength: float = 5, **kwargs):
        super().__init__(*args, **kwargs)
        self.strength = strength

    def for_every_object(self, obj: GameObject, dt: float):
        obj.update(dt)
        # Clamp objects inside world bounds
        # if the object is not an outsider
        if not obj.outsider:
            obj.rect.clamp_ip(pygame.Rect(0, 0, self.width, self.height))

        # Apply gravity to the object
        gravity_force = pygame.Vector2(0, self.strength * dt)
        obj.velocity += gravity_force

        # Cam follow if True
        if self.camera_follow:
            self.camera.update(dt)

    def update(self, dt: float):
        super().update(dt)
