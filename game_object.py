import pygame


class GameObject:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: tuple[int, int, int] = (255, 255, 255),
        outsider: bool = False,
    ):
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = pygame.Vector2(0, 0)
        self.angle = 0  # rotation angle in degrees
        self.outsider = outsider

        # Single frame of solid color
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill(self.color)
        self._surface = surface

        # Initialize mask with the surface
        self.mask = pygame.mask.from_surface(self._surface)

    def update(self, dt: float):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt
        self._update_rect_and_mask()

    def draw(
        self,
        surface: pygame.Surface,
        camera_offset: tuple[int, int] = (0, 0),
        rotation: float = 0,
    ):
        rotated_image = pygame.transform.rotate(self._surface, -(self.angle + rotation))
        draw_pos = pygame.Vector2(self.rect.topleft) - camera_offset
        draw_rect = rotated_image.get_rect(
            center=(
                draw_pos.x + self.width / 2,
                draw_pos.y + self.height / 2,
            )
        )
        surface.blit(rotated_image, draw_rect.topleft)

    def rotate(self, degrees: float):
        self.angle = (self.angle + degrees) % 360
        self._update_rect_and_mask()

    def collides_with(self, other: "GameObject") -> bool:
        offset = (int(other.rect.x - self.rect.x), int(other.rect.y - self.rect.y))
        return self.mask.overlap(other.mask, offset) is not None

    def mirror(self, axis: str):
        if axis.lower() == "x":
            self._surface = pygame.transform.flip(self._surface, True, False)
        elif axis.lower() == "y":
            self._surface = pygame.transform.flip(self._surface, False, True)
        else:
            raise ValueError("Axis must be 'x' or 'y'.")
        self._update_rect_and_mask()

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, x: int):
        self.rect.x = x

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, y: int):
        self.rect.y = y

    def _update_rect_and_mask(self):
        self.rect = self._surface.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self._surface)
