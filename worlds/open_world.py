from pynolad.camera import Camera
from pynolad.game_object import GameObject

from .world import World


class OpenWorld(World):
    def __init__(
        self,
        objects: list[GameObject] = [],
        camera: Camera = None,
    ):
        super().__init__(objects=objects, camera=camera)
