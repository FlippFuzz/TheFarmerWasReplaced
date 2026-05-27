from __builtins__ import (
    Any,
    East,
    Entities,
    Entity,
    Grounds,
    Items,
    can_harvest,
    clear,
    get_companion,
    get_ground_type,
    get_water,
    get_world_size,
    harvest,
    move,
    num_drones,
    plant,
    spawn_drone,
    till,
    use_item,
)
from constants_poly import poly_pattern
from utils import move_to


def drone_plant_row(y: int, rowData: list[Entity], world_size: int) -> Any:
    move_to(0, y, world_size)
    for x in range(world_size):
        to_plant = rowData[x]
        if get_ground_type() != Grounds.Soil:
            till()
        plant(to_plant)
        move(East)


def drone_harvest():
    while not can_harvest():
        pass
    harvest()


def drone_reroll(target_plant: Entity, map: list[list[Entity]]):
    while True:
        harvest()
        plant(target_plant)
        companion = get_companion()
        if companion:
            comp_plant, (comp_x, comp_y) = companion
            map_comp_plant = map[comp_y][comp_x]
            if map_comp_plant == comp_plant:
                break

    # Water if needed
    if get_water() < 0.75:
        use_item(Items.Water)


def drone_poly(
    poly_spot: tuple[int, int],
    map: list[list[Entity]],
    target_plant: Entity,
    world_size: int,
):
    x, y = poly_spot
    move_to(x, y, world_size)

    while True:
        # Reroll and wait for harvest
        drone_reroll(target_plant, map)
        while not can_harvest():
            pass  # Wait until ready to harvest
        harvest()


def generate_poly_pattern(
    world_size=32,
    plant=Entities.Carrot,
    pattern=[Entities.Grass, Entities.Bush, Entities.Tree],
    num_plants=1,
):
    state = []
    poly_spots = []
    for y in range(world_size):
        current_y = []
        yMod = y % 4
        for x in range(world_size):
            if yMod < 3:
                # The whole row is either G, B or T
                current_y.append(pattern[yMod])
            else:
                xMod = x % 7
                x_start_inc = 3 - (num_plants // 2)
                x_end_exc = x_start_inc + num_plants

                if xMod == 3:
                    poly_spots.append((x, y))

                if xMod >= x_start_inc and xMod < x_end_exc:
                    if plant == Entities.Tree and xMod % 2 == 1:
                        # We only want to plant in 1,3,5 or 7 when trees
                        current_y.append(plant)
                    else:
                        current_y.append(pattern[x % 3])
                elif xMod < 3:
                    current_y.append(pattern[xMod])
                else:
                    current_y.append(pattern[xMod - 4])

        state.append(current_y)

    return state, poly_spots


def farm_poly(target_plant: Entity = Entities.Carrot):
    world_size = get_world_size()
    poly_spots, map = poly_pattern(target_plant, world_size)

    # 1. Setup farm as per poly pattern
    # Each drone is to plant a row
    # for y in range(world_size - 1, -1, -1):
    for y in range(world_size):
        if not spawn_drone(drone_plant_row, y, map[y], world_size):
            drone_plant_row(y, map[y], world_size)

    while num_drones() != 1:
        pass  # Just waiting the setup to be complete

    # 2. Each drone is to poly on their own grid
    for spot in poly_spots:
        if not spawn_drone(drone_poly, spot, map, target_plant, world_size):
            drone_poly(spot, map, target_plant, world_size)
            break


if __name__ == "__main__":
    clear()
    farm_poly(Entities.Carrot)
    # farm_poly(Entities.Tree, 5)
    # farm_poly(Entities.Grass)
