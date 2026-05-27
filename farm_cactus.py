from __builtins__ import (
    Drone,
    East,
    Entities,
    Grounds,
    South,
    West,
    clear,
    get_ground_type,
    get_world_size,
    harvest,
    measure,
    move,
    plant,
    spawn_drone,
    swap,
    till,
    wait_for,
)
from utils import move_to


def _drone_plant_measure_cactus(row_y: int, world_size: int) -> tuple:
    # Plant and measure sunflowers
    move_to(0, row_y, world_size)
    measurements: list[tuple[int, int]] = []

    for _ in range(world_size):
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Cactus)
        size = measure()
        measurements.append(size)  # type: ignore - We know size is int
        move(East)

    return row_y, measurements


def _locate_first_unsorted(data: list[int], start_pos: int, world_size: int) -> int:
    # Find the first smallest and return it's position
    pos = -1
    smallest = 9999
    for i in range(start_pos, world_size):
        cur = data[i]
        if cur < smallest:
            smallest = cur
            pos = i
    return pos


def _drone_sort_row(row_y: int, world_map: list[list[int]], world_size: int) -> tuple:
    row_map = world_map[row_y]

    for i in range(world_size):
        # Find the (first) smallest cactus from i to the right of the map
        pos = _locate_first_unsorted(row_map, i, world_size)

        # Then, move the smallest cactus to i
        move_to(pos, row_y, world_size)
        for i in range(pos, i, -1):
            # Update memory (so that we don't need to measure again)
            cur_size = row_map[i]
            i1 = i - 1  # Just optimization to save 1 tick
            row_map[i] = row_map[i1]
            row_map[i1] = cur_size

            # Do the actual swap
            swap(West)
            move(West)

    # Return the updated size data. We swapped our local memory, and the world map needs updating
    return row_y, row_map


def _drone_sort_col(col_x: int, col_map: list[int], world_size: int):
    for i in range(world_size):
        # Find the (first) smallest cactus from i to the top of the map
        pos = _locate_first_unsorted(col_map, i, world_size)

        # Then, move the smallest cactus to i
        move_to(col_x, pos, world_size)
        for i in range(pos, i, -1):
            # Update memory (so that we don't need to measure again)
            cur_size = col_map[i]
            i1 = i - 1  # Just optimization to save 1 tick
            col_map[i] = col_map[i1]
            col_map[i1] = cur_size

            # Do the actual swap
            swap(South)
            move(South)

    # No need to return updated col_map. We are done after this


if __name__ == "__main__":
    clear()
    world_size = get_world_size()

    world_map: list[list[int]] = []
    for _ in range(world_size):
        world_map.append([])

    while True:
        # Handles
        planting_handles: list[Drone] = []
        row_sort_handles: list[Drone] = []
        col_sort_handles: list[Drone] = []

        # Start planting and measuring cactus
        for y in range(world_size):
            planting_handle = spawn_drone(_drone_plant_measure_cactus, y, world_size)
            if planting_handle:
                planting_handles.append(planting_handle)
            else:
                _, local_measurement = _drone_plant_measure_cactus(y, world_size)  # type: ignore
                world_map[y] = local_measurement

        # Wait for planting to finish and collect all measurements
        for handle in planting_handles:
            y, local_measurement = wait_for(handle)  # type: ignore
            world_map[y] = local_measurement

        # Sort the rows
        for y in range(world_size):
            row_sort_handle = spawn_drone(_drone_sort_row, y, world_map, world_size)
            if row_sort_handle:
                row_sort_handles.append(row_sort_handle)
            else:
                _, local_measurement = _drone_sort_row(y, world_map, world_size)
                world_map[y] = local_measurement

        # Wait for row sorting to finish and update world map
        for row_sort_handle in row_sort_handles:
            y, local_measurement = wait_for(row_sort_handle)  # type: ignore
            world_map[y] = local_measurement

        # TODO: Can we optimize here?
        # Perhaps we can start sorting columns once we have free drones + columns are complete?

        # Sort the columns
        for x in range(world_size):
            col_map: list[int] = []
            for y in range(world_size):
                col_map.append(world_map[y][x])

            col_sort_handle = spawn_drone(_drone_sort_col, x, col_map, world_size)
            if col_sort_handle:
                col_sort_handles.append(col_sort_handle)
            else:
                _drone_sort_col(x, col_map, world_size)

        # Wait for col sorting to finish
        for col_sort_handle in col_sort_handles:
            wait_for(col_sort_handle)

        harvest()
