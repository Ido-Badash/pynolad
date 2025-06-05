import pygame

from .game_object import GameObject


class Camera:
    def __init__(
        self,
        width: int,
        height: int,
        target: GameObject = None,
        smooth_speed: float = 0.1,
    ):
        self.offset = pygame.Vector2(0, 0)
        self.target = target
        self.width = width
        self.height = height
        self.smooth_speed = smooth_speed
        self.rotation = 0.0  # degrees

    def update(self):
        if self.target:
            target_center = pygame.Vector2(self.target.rect.center)
            visible_w = self.width
            visible_h = self.height
            target_offset = target_center - pygame.Vector2(visible_w / 2, visible_h / 2)
            # Linear interpolation for smooth movement
            self.offset += (target_offset - self.offset) * self.smooth_speed

    def rotate(self, degrees: float):
        self.rotation = (self.rotation + degrees) % 360

    def attach(self, obj: GameObject):
        self.target = obj

    def detach(self):
        self.target = None
