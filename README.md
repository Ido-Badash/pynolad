# Pynolad Game Framework

This project is a simple 2D game framework built with [Pygame](https://www.pygame.org/). It features animated game objects, a camera system, collision detection, and a basic game loop.

## Features

- **Animated Sprites**: Easily load and animate sprite frames.
- **Camera System**: Smooth camera following a target object.
- **Pixel-Perfect Collision**: Uses masks for accurate collision detection.
- **GameObject Class**: Handles movement, animation, rotation, and mirroring.
- **World Management**: Add and update multiple objects in a world.

## Getting Started

### Prerequisites

- Python 3.8+
- Pygame (`pip install pygame`)

### Running the Game

1. Place your player animation frames in the `assets` folder (named `player_0.png`, `player_1.png`, ...).
2. Run the main file:

   ```bash
   python main.py
   ```

### Controls

- **WASD**: Move the player
- **Player resets** to the starting position if it collides with the red box.

## Project Structure

```
test2/
│
├── main.py                # Main game loop and logic
├── assets/                # Place your sprite images here
└── pynolad/
    ├── __init__.py
    ├── camera.py          # Camera class
    ├── game_object.py     # GameObject class
    ├── world.py           # World management classes
    └── README.md          # This file
```

## Customization

- Add more objects by creating new `GameObject` instances and adding them to the world.
- Customize the camera by changing its target or smooth speed.
- Extend the `GameObject` class for more behaviors.

## License

MIT License

---

Made with ❤️ using Pygame.