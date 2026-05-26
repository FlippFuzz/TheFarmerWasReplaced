from __builtins__ import (
    East,
    North,
    South,
    West,
    get_pos_x,
    get_pos_y,
    move,
)


def move_to(x: int, y: int, world_size: int):
    # Calculating this once saves 1 tick compared to doing it inside each axis check.
    half_word_size = world_size // 2

    # X movement: (target - current) % world_size gives the distance moving East.
    dx = (x - get_pos_x()) % world_size
    if dx > half_word_size:  # Faster to loop around the other direction
        for _ in range(world_size - dx):
            move(West)
    else:
        for _ in range(dx):
            move(East)

    # Y movement: (target - current) % world_size gives the distance moving North.
    dy = (y - get_pos_y()) % world_size
    if dy > half_word_size:  # Faster to loop around the other direction
        for _ in range(world_size - dy):
            move(South)
    else:
        for _ in range(dy):
            move(North)
