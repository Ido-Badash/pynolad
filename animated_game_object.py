import pygame

from .game_object import GameObject


class AnimatedGameObject(GameObject):
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
        super().__init__(x, y, width, height, color, outsider)
        self.image_paths = image_paths if image_paths is not None else []
        self.animation_fps = animation_fps
        self.with_animation = with_animation

        self.frames: list[pygame.Surface] = []
        if image_paths:
            for path in image_paths:
                try:
                    img = pygame.image.load(path).convert_alpha()
                    img = pygame.transform.scale(img, (width, height))
                    self.frames.append(img)
                except pygame.error as e:
                    print(f"Warning: Could not load image {path}: {e}")
                    surface = pygame.Surface((width, height), pygame.SRCALPHA)
                    surface.fill(self.color)
                    self.frames.append(surface)
            if not self.frames:
                surface = pygame.Surface((width, height), pygame.SRCALPHA)
                surface.fill(self.color)
                self.frames.append(surface)
        else:
            surface = pygame.Surface((width, height), pygame.SRCALPHA)
            surface.fill(self.color)
            self.frames.append(surface)

        self._frame_index = 0
        self.animation_timer = 0.0

        # Use the first frame as the surface for the parent
        self._surface = self.frames[self._frame_index]
        self.mask = pygame.mask.from_surface(self._surface)

    def update(self, dt: float):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

        if len(self.frames) > 1 and self.with_animation:
            self.animation_timer += dt
            if self.animation_timer >= 1 / self.animation_fps:
                self._frame_index = (self._frame_index + 1) % len(self.frames)
                self.animation_timer = 0.0

        self._surface = self.frames[self._frame_index]
        self._update_rect_and_mask()

    def mirror(self, axis: str):
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
        self._surface = self.frames[self._frame_index]
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
            self._surface = frame
            self._update_rect_and_mask()
