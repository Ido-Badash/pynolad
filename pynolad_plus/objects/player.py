import pygame

import pynolad

from .interactable import Interactable


class Player(pynolad.AnimatedGameObject):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        colliders: list[Interactable] = [],
        speed=35,
        *args,
        **kwargs
    ):
        super().__init__(x, y, width, height, *args, **kwargs)
        self.colliders = colliders
        self.speed = speed * 1000

    def handle_movement(self, dt):
        keys = pygame.key.get_pressed()
        input_vector = pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_a], keys[pygame.K_s] - keys[pygame.K_w]
        )
        if input_vector.length() > 0:
            input_vector.normalize_ip()
        self.velocity.x = input_vector.x * self.speed * dt
        self.velocity.y = input_vector.y * self.speed * dt

    def handle_collision(self):
        """Handle all player collisions"""
        for collider in self.colliders:
            if self.collides_with(collider):
                # Reset position to a safe location
                collider.interact()
