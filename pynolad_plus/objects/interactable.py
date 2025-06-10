from typing import Callable

import pygame
import pynolad


class Interactable(pynolad.GameObject):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        on_interaction: Callable[[], None] = lambda: None,
        *args,
        **kwargs
    ):
        super().__init__(x, y, width, height, *args, **kwargs)
        self.on_interaction = on_interaction

    def set_on_interaction(self, new_on_interaction: Callable[[], None]):
        self.on_interaction = new_on_interaction

    def interact(self):
        self.on_interaction()
