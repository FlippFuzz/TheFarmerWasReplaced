from __builtins__ import (
    Direction,
    Hats,
    North,
    change_hat,
    get_pos_x,
    get_pos_y,
    measure,
    move,
    set_world_size,
)
from constants_bones import get_map


def farm_bones_single(world_size: int, map: list[list[Direction]]):
    change_hat(Hats.Dinosaur_Hat)  # Start dinosaur


def farm_bones(world_size: int):
    set_world_size(world_size)
    map = get_map(world_size)

    # Precalc some values
    world_size_1 = world_size - 1
    max_length = world_size * world_size
    max_length_1 = max_length - 1
    max_length_p80 = max_length * 0.8
    skip_length = (world_size - 2) * 2

    while True:
        change_hat(Hats.Dinosaur_Hat)  # Start dinosaur

        # Variables
        apple: tuple[int, int] = measure()  # type: ignore
        apple_x, apple_y = apple
        length = 0
        num_skips = 0

        while True:
            x = get_pos_x()
            y = get_pos_y()

            if apple_x == x and apple_y == y:
                apple: tuple[int, int] = measure()  # type: ignore
                if apple == None:  # noqa: E711 - Game doesn't support "apple is None"
                    change_hat(Hats.Straw_Hat)  # End dinosaur
                    break
                apple_x, apple_y = apple
                length += 1
                num_skips = 0

            # Allow shortcut at the rightmost column
            # We just go north instead of looping left and back to the right
            skip_taken = False
            if y % 2 == 0:
                # Optimization: Don't use shortcuts when snake is long
                # When the snake is long, we want the snake to be tightly looped
                # so that the apples will keep appearing in front.
                # We don't want the apples to appear in a gap that is behind the head of the snake.
                if length < max_length_p80:
                    if x == world_size_1:
                        if apple_x != 0:
                            if apple_y > y:
                                # Apple is north of the snake.
                                # We can cut across some snake rows.
                                while num_skips * skip_length + length < max_length_1:
                                    y_next = y + 2
                                    if y_next < apple_y:
                                        move(North)
                                        move(North)
                                        y = y_next
                                        num_skips += 1
                                        skip_taken = True
                                    else:
                                        break
                            elif apple_y < y:
                                # Apple is south of the snake.
                                # The shortcut is to move north asap to wrap around the world
                                while num_skips * skip_length + length < max_length_1:
                                    y_next = y + 2
                                    if y_next < world_size_1:
                                        move(North)
                                        move(North)
                                        y = y_next
                                        num_skips += 1
                                        skip_taken = True
                                    else:
                                        break
                        elif apple_x == 0:
                            # The apple is on the return path to south.
                            # The shortcut is to move north ASAP so that we hit the return path
                            while num_skips * skip_length + length < max_length_1:
                                y_next = y + 2
                                if y_next < world_size_1:
                                    move(North)
                                    move(North)
                                    y = y_next
                                    num_skips += 1
                                    skip_taken = True
                                else:
                                    break

            if not skip_taken:
                dir = map[y][x]
                if not move(dir):
                    change_hat(Hats.Straw_Hat)  # End dinosaur
                    break


if __name__ == "__main__":
    farm_bones(32)
