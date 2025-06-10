import pynolad


class RectBorder:
    def __init__(
        self,
        surface_w: int,
        surface_h: int,
        weight: int = 10,
        start_from: tuple = (0, 0),
        top_color=(255, 0, 0),
        left_color=(255, 0, 0),
        right_color=(255, 0, 0),
        bottom_color=(255, 0, 0),
    ):
        self.surface_w = surface_w
        self.surface_h = surface_h
        self.weight = weight
        self.start_from = start_from
        self.top_color = top_color
        self.left_color = left_color
        self.right_color = right_color
        self.bottom_color = bottom_color

        self.start_x = start_from[0]
        self.start_y = start_from[1]

        self.borders = self._create_borders()

    def _create_borders(self):
        w, h, weight = self.surface_w, self.surface_h, self.weight
        return [
            # Top
            pynolad.GameObject(
                self.start_x,
                -weight + self.start_y,
                w + weight,
                weight,
                color=self.top_color,
                outsider=True,
            ),
            # Left
            pynolad.GameObject(
                -weight + self.start_x,
                -weight + self.start_y,
                weight,
                h + weight,
                color=self.left_color,
                outsider=True,
            ),
            # Right
            pynolad.GameObject(
                w + self.start_x,
                self.start_y,
                weight,
                h + weight,
                color=self.right_color,
                outsider=True,
            ),
            # Bottom
            pynolad.GameObject(
                -weight + self.start_x,
                h + self.start_y,
                w + weight,
                weight,
                color=self.bottom_color,
                outsider=True,
            ),
        ]

    def get_borders(self):
        return self.borders
