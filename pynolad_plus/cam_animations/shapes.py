import math

import pynolad


def circle_cam_animation(
    surf_w: int,
    surf_h: int,
    camera: pynolad.Camera,
    obj: pynolad.GameObject,
    radius: float = 25,
    angle: float = 0,
):
    # Calculate camera position in a circle around the player
    obj_center_x = obj.x + obj.width // 2
    obj_center_y = obj.y + obj.height // 2

    cam_x = obj_center_x + radius * math.cos(angle) - surf_w // 2
    cam_y = obj_center_y + radius * math.sin(angle) - surf_h // 2

    camera.set_pos((cam_x, cam_y))
