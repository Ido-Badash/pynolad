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
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_paths = image_paths if image_paths is not None else []
        self.animation_fps = animation_fps
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = pygame.Vector2(0, 0)
        self.angle = 0  # rotation angle in degrees
        self.with_animation = with_animation

        self.frames = []
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
                    surface.fill(color)
                    self.frames.append(surface)
            if (
                not self.frames
            ):  # If no images loaded successfully, default to a single color frame
                surface = pygame.Surface((width, height), pygame.SRCALPHA)
                surface.fill(color)
                self.frames.append(surface)
        else:
            # Single frame of solid color if no image paths provided
            surface = pygame.Surface((width, height), pygame.SRCALPHA)
            surface.fill(color)
            self.frames.append(surface)

        self.frame_index = 0
        self.animation_timer = 0.0

        # Initialize mask with the first frame
        self.mask = pygame.mask.from_surface(self.frames[0])

    def update(self, dt: float):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

        if len(self.frames) > 1 and self.with_animation:
            self.animation_timer += dt
            if self.animation_timer >= 1 / self.animation_fps:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.animation_timer = 0.0

        # Update mask to the current frame for collision detection
        self.mask = pygame.mask.from_surface(self.frames[self.frame_index])

    def draw(
        self,
        surface: pygame.Surface,
        camera_offset: tuple[int, int] = (0, 0),
        rotation: float = 0,  # Corrected parameter name from 'roatation'
    ):
        # Get the current frame for drawing
        frame = self.frames[self.frame_index]

        # Apply rotation (object's own rotation + external rotation)
        # Note: Pygame rotation is counter-clockwise, so -self.angle
        rotated_image = pygame.transform.rotate(frame, -(self.angle + rotation))

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

        # Update the mask after mirroring
        self.mask = pygame.mask.from_surface(self.frames[self.frame_index])
