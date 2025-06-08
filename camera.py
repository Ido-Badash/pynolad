import pygame

from .game_object import GameObject


class Camera:
    def __init__(
        self,
        width: int,
        height: int,
        target: GameObject = None,
        smooth_speed: float = 3,
    ):
        self._x = 0
        self._y = 0
        self._offset = pygame.Vector2(self.x, self.y)
        self.target = target
        self.width = width
        self.height = height
        self.smooth_speed = smooth_speed
        self.rotation = 0.0  # degrees

    def update(self, dt=None):
        if self.target:
            target_center = pygame.Vector2(self.target.rect.center)
            visible_w = self.width
            visible_h = self.height
            target_offset = target_center - pygame.Vector2(visible_w / 2, visible_h / 2)
            # Linear interpolation for smooth movement
            speed = self.smooth_speed
            if dt is not None:
                speed *= dt
            self.offset += (target_offset - self.offset) * speed
            self.x = int(self.offset.x)
            self.y = int(self.offset.y)
        else:
            # If no target keep the camera at its current position
            self.offset = pygame.Vector2(self.x, self.y)

    def rotate(self, degrees: float):
        self.rotation = (self.rotation + degrees) % 360

    def attach(self, obj: GameObject):
        self.target = obj

    def detach(self):
        self.target = None

    def set_pos(self, offset: tuple[int, int]):
        """
        This will not work if there is an active target,
        Use the `detach` method so it will work
        """
        if self.target:
            self.x = self.target.x + offset[0]
            self.y = self.target.y + offset[1]
        else:
            self.x = offset[0]
            self.y = offset[1]

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, offset: pygame.Vector2 = None):
        if offset is None:
            self._offset = pygame.Vector2(self.x, self.y)
            return
        x = self.x if offset[0] is None else offset[0]
        y = self.y if offset[1] is None else offset[1]
        self._offset = pygame.Vector2(x, y)
