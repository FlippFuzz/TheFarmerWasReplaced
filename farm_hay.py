from __builtins__ import (
    East,
    Entities,
    Grounds,
    Items,
    South,
    can_harvest,
    clear,
    get_ground_type,
    get_world_size,
    harvest,
    move,
    num_items,
    plant,
    till,
)


def farm_hay(stop_qty: int):
    clear()
    world_size = get_world_size()

    while num_items(Items.Hay) < stop_qty:
        for _ in range(world_size):
            move(East)
            for _ in range(world_size):
                move(South)
                if get_ground_type() != Grounds.Grassland:
                    till()
                if can_harvest():
                    harvest()
                    plant(Entities.Grass)


if __name__ == "__main__":
    farm_hay(100000000)
