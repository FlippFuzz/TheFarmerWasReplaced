from __builtins__ import (
    Hats,
    change_hat,
    get_pos_x,
    get_pos_y,
    measure,
    move,
    set_world_size,
)
from constants_bones import get_map_16


def farm_bones(world_size: int):
    set_world_size(world_size)
    map = get_map_16()
    change_hat(Hats.Dinosaur_Hat)  # Start dinosaur

    apple: tuple[int, int] = measure()  # type: ignore
    apple_x, apple_y = apple
    length = 0

    x = get_pos_x()
    y = get_pos_y()

    while True:
        if apple_x == x and apple_y == y:
            apple: tuple[int, int] = measure()  # type: ignore
            apple_x, apple_y = apple
            length += 1

        dir = map[y][x]
        if not move(dir):
            set_world_size(world_size)
            change_hat(Hats.Dinosaur_Hat)


if __name__ == "__main__":
    farm_bones(16)
