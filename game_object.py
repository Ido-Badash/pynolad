import pygame


class GameObject:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        image_paths: list[str] = None,
        animation_fps: int = 10,
        color: tuple[int, int, int] = (255, 255, 255),
        with_animation: bool = True,
        outsider: bool = False,
    ):
        self.width = width
        self.height = height
        self.image_paths = image_paths if image_paths is not None else []
        self.animation_fps = animation_fps
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = pygame.Vector2(0, 0)
        self.angle = 0  # rotation angle in degrees
        self.with_animation = with_animation
        self.outsider = outsider

        self.frames: list[pygame.Surface] = []
        if image_paths:
            for path in image_paths:
                try:
                    img = pygame.image.load(path).convert_alpha()
                    img = pygame.transform.scale(img, (width, height))
                    self.frames.append(img)
                except pygame.error as e:
                    print(f"Warning: Could not load image {path}: {e}")
                    # Fallback to a solid color if image loading fails for a frame
                    surface = pygame.Surface((width, height), pygame.SRCALPHA)
                    surface.fill(self.color)
                    self.frames.append(surface)
            if (
                not self.frames
            ):  # If no images loaded successfully, default to a single color frame
                surface = pygame.Surface((width, height), pygame.SRCALPHA)
                surface.fill(self.color)
                self.frames.append(surface)
        else:
            # Single frame of solid color if no image paths provided
            surface = pygame.Surface((width, height), pygame.SRCALPHA)
            surface.fill(self.color)
            self.frames.append(surface)

        self._frame_index = 0
        self.animation_timer = 0.0

        # Initialize mask with the first frame
        self.mask = pygame.mask.from_surface(self.current_frame)

    def update(self, dt: float):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

        if len(self.frames) > 1 and self.with_animation:
            self.animation_timer += dt
            if self.animation_timer >= 1 / self.animation_fps:
                self._frame_index = (self._frame_index + 1) % len(self.frames)
                self.animation_timer = 0.0

        self._update_rect_and_mask()

    def draw(
        self,
        surface: pygame.Surface,
        camera_offset: tuple[int, int] = (0, 0),
        rotation: float = 0,  # Corrected parameter name from 'roatation'
    ):

        # Apply rotation (object's own rotation + external rotation)
        # Note: Pygame rotation is counter-clockwise, so -self.angle
        rotated_image = pygame.transform.rotate(
            self.current_frame, -(self.angle + rotation)
        )

        # Calculate drawing position relative to camera and apply external rotation
        draw_pos = pygame.Vector2(self.rect.topleft) - camera_offset

        # Get the rect for the rotated image, centered at the calculated position
        draw_rect = rotated_image.get_rect(
            center=(
                draw_pos.x + self.width / 2,
                draw_pos.y + self.height / 2,
            )
        )
        surface.blit(rotated_image, draw_rect.topleft)

    def rotate(self, degrees: float):
        """Rotates the GameObject by the given degrees (updates its internal angle)."""
        self.angle = (self.angle + degrees) % 360

    def collides_with(self, other: "GameObject") -> bool:
        """Performs pixel-perfect collision detection using masks."""
        offset = (int(other.rect.x - self.rect.x), int(other.rect.y - self.rect.y))
        return self.mask.overlap(other.mask, offset) is not None

    def mirror(self, axis: str):
        """Mirrors the GameObject across the specified axis ('x' or 'y')."""
        if axis.lower() == "x":
            self.frames = [
                pygame.transform.flip(frame, True, False) for frame in self.frames
            ]
        elif axis.lower() == "y":
            self.frames = [
                pygame.transform.flip(frame, False, True) for frame in self.frames
            ]
        else:
            raise ValueError("Axis must be 'x' or 'y'.")

        self._update_rect_and_mask()

    def get_frame(self, frame_idx: int) -> pygame.Surface:
        return self.frames[frame_idx % len(self.frames)]

    def set_frame(self, frame_idx: int, new_surface: pygame.Surface):
        self.frames[frame_idx] = new_surface

    @property
    def current_frame(self) -> pygame.Surface:
        return self.frames[self._frame_index]

    @current_frame.setter
    def current_frame(self, frame: pygame.Surface):
        if self.frames:
            self.frames[self._frame_index] = frame
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
        self.rect = self.current_frame.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.current_frame)
