from __builtins__ import (
    Any,
    East,
    Entities,
    Grounds,
    can_harvest,
    clear,
    get_ground_type,
    get_world_size,
    harvest,
    max_drones,
    measure,
    move,
    num_drones,
    plant,
    spawn_drone,
    till,
    wait_for,
)
from utils import move_to


def drone_plant_measure_sunflowers(row_y: int, world_size: int) -> Any:
    # Plant and measure sunflowers
    move_to(0, row_y, world_size)
    measurements: dict[int, list[tuple[int, int]]] = {
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: [],
    }
    for x in range(world_size):
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Sunflower)
        petals = measure()
        measurements[petals].append((x, row_y))  # type: ignore - We know petals is int
        move(East)

    return measurements  # type: ignore - We know this can be casted to Any


def drone_harvest(data: list[tuple[int, int]], world_size: int):
    for pos in data:
        x, y = pos
        move_to(x, y, world_size)
        while not can_harvest():
            pass  # Wait for plant to grow to be able to harvest
        harvest()


def combine_measurements(
    result: dict[int, list[tuple[int, int]]], data: dict[int, list[tuple[int, int]]]
):
    for petal_count in range(7, 16, 1):
        for pos in data[petal_count]:
            result[petal_count].append(pos)


def split_list(
    input_list: list[tuple[int, int]], num_chunks: int
) -> list[list[tuple[int, int]]]:
    length = len(input_list)

    # 1. Calculate the base size of every chunk
    base_size = length // num_chunks

    # 2. Calculate how many chunks need to hold 1 extra item
    extra = length % num_chunks

    result = []
    start = 0

    for i in range(num_chunks):
        # Determine the size of the current chunk:
        # If the current index (i) is less than 'extra', add 1 to the base size
        current_size = base_size
        if i < extra:
            current_size += 1

        end = start + current_size
        result.append(input_list[start:end])
        start = end

    return result


if __name__ == "__main__":
    clear()
    world_size = get_world_size()

    while True:
        planting_handles = []
        measurements: dict[int, list[tuple[int, int]]] = {
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: [],
            13: [],
            14: [],
            15: [],
        }

        for y in range(world_size):
            handle = spawn_drone(drone_plant_measure_sunflowers, y, world_size)
            if handle:
                planting_handles.append(handle)
            else:
                local_measurement = drone_plant_measure_sunflowers(y, world_size)
                combine_measurements(measurements, local_measurement)

        # Wait for planting to finish and collect all measurements
        for handle in planting_handles:
            row_results = wait_for(handle)
            combine_measurements(measurements, row_results)

        # Now, start harvesting starting from petals 15
        max_num_drones = max_drones()
        for i in range(15, 6, -1):
            # quick_print("Working on petals: " + str(i))
            positions = measurements[i]
            splits = split_list(positions, max_num_drones)
            for split in splits:
                # quick_print(split)
                if not spawn_drone(drone_harvest, split, world_size):
                    drone_harvest(split, world_size)

            # Wait for all to complete
            while num_drones() != 1:
                pass
