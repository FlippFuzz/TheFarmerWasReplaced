import builtins
from typing import Literal

N = "N"
B = "B"
C = "C"
G = "G"
T = "T"
type PlantType = Literal["B", "C", "G", "T"]


def generate_poly_spots(world_size: int = 32) -> list[tuple[int, int]]:
    results = {
        32: [
            (0, 0),
            (8, 0),
            (16, 0),
            (24, 0),
            (4, 4),
            (12, 4),
            (20, 4),
            (28, 4),
            (0, 8),
            (8, 8),
            (16, 8),
            (24, 8),
            (4, 12),
            (12, 12),
            (20, 12),
            (28, 12),
            (0, 16),
            (8, 16),
            (16, 16),
            (24, 16),
            (4, 20),
            (12, 20),
            (20, 20),
            (28, 20),
            (0, 24),
            (8, 24),
            (16, 24),
            (24, 24),
            (4, 28),
            (12, 28),
            (20, 28),
            (28, 28),
        ],
        22: [
            (0, 0),
            (7, 1),
            (16, 1),
            (3, 4),
            (12, 4),
            (19, 5),
            (8, 7),
            (15, 8),
            (0, 9),
            (11, 11),
            (5, 12),
            (18, 12),
            (1, 15),
            (14, 15),
            (8, 16),
            (19, 18),
            (4, 19),
            (11, 20),
        ],
        16: [(0, 0), (5, 3), (12, 3), (10, 8), (1, 9), (13, 12), (4, 13), (9, 15)],
        12: [(0, 0), (8, 4), (2, 5), (6, 11)],
        8: [(0, 0), (4, 4)],
    }

    return results.get(world_size, [])


def generate_poly_pattern(
    world_size: int = 32, plant: PlantType = C
) -> list[list[builtins.str]]:
    state: list[list[builtins.str]] = []

    # Fill the 2D list with "N"s to indicate empty
    for _ in range(world_size):
        state.append([N] * world_size)

    patterns = {  # B C G T
        B: [  # C G T
            [N, N, N, C, N, N, N],
            [N, N, G, G, G, N, N],
            [N, T, T, T, T, T, N],
            [C, G, T, B, C, G, T],
            [N, C, C, C, C, C, N],
            [N, N, G, G, G, N, N],
            [N, N, N, T, N, N, N],
        ],
        C: [  # B G T
            [N, N, N, B, N, N, N],
            [N, N, G, G, G, N, N],
            [N, T, T, T, T, T, N],
            [B, G, T, C, B, G, T],
            [N, B, B, B, B, B, N],
            [N, N, G, G, G, N, N],
            [N, N, N, T, N, N, N],
        ],
        G: [  # B C T
            [N, N, N, B, N, N, N],
            [N, N, C, C, C, N, N],
            [N, T, T, T, T, T, N],
            [B, C, T, G, B, C, T],
            [N, B, B, B, B, B, N],
            [N, N, C, C, C, N, N],
            [N, N, N, T, N, N, N],
        ],
        T: [  # B C G
            [N, N, N, B, N, N, N],
            [N, N, C, C, C, N, N],
            [N, G, G, G, G, G, N],
            [B, C, G, T, B, C, G],
            [N, B, B, B, B, B, N],
            [N, N, C, C, C, N, N],
            [N, N, N, G, N, N, N],
        ],
    }

    pattern = patterns[plant]

    # Now, we iterate through all the poly spots and copy the pattern to our state array
    poly_spots = generate_poly_spots(world_size)
    for spot in poly_spots:
        spot_x, spot_y = spot
        for index_y in range(7):
            for index_x in range(7):
                if pattern[index_y][index_x] == N:
                    continue  # Don't copy if none

                y = (spot_y + index_y - 3) % world_size
                x = (spot_x + index_x - 3) % world_size
                state[y][x] = pattern[index_y][index_x]

    return state


def print_state(state):
    for row in builtins.reversed(state):
        # Joins the elements of the row with a space for a clean grid output
        print(" ".join(row))


def print_function(world_size: int, plant: PlantType):
    poly_spots = generate_poly_spots(world_size)
    state = generate_poly_pattern(world_size, plant)

    print(
        f"def _plant_{world_size}_{plant}()  "
        "-> tuple[list[tuple[int, int]], list[list[Entity]]]:"
    )
    print("    # fmt: off")
    print("    return (")
    print(f"        {poly_spots}, ")
    print("        [")
    for row in state:
        row_str = "            ["
        for element in row:
            row_str += f"{element}, "
        print(row_str + "], ")
    print("        ]")
    print("    )")
    print("    # fmt: on")
    print("")
    print("")


if __name__ == "__main__":
    print("from __builtins__ import Entities, Entity")
    print("")
    print("B = Entities.Bush")
    print("C = Entities.Carrot")
    print("G = Entities.Grass")
    print("T = Entities.Tree")
    print("N = Entities.Grass # N actually means empty, but easier to just be grass")
    print("")
    print("")

    for world_size in [32, 22, 16, 12, 8]:
        for plant in [B, C, G, T]:
            state = generate_poly_pattern(world_size, plant)
            print_function(world_size, plant)

    for world_size in [32, 22, 16, 12, 8]:
        print(
            f"def _plant_{world_size}(plant: Entity) -> tuple[list[tuple[int, int]], list[list[Entity]]]:"
        )
        print(
            f"    switcher = {{B: _plant_{world_size}_B, C: _plant_{world_size}_C, G: _plant_{world_size}_G, T: _plant_{world_size}_T}}"
        )
        print("    return switcher[plant]()")
        print("")
        print("")

    print("def poly_pattern(")
    print("plant: Entity, world_size: int")
    print(") -> tuple[list[tuple[int, int]], list[list[Entity]]]:")
    print(
        "    switcher = {32: _plant_32, 22: _plant_22, 16: _plant_16, 12: _plant_12, 8: _plant_8}"
    )
    print("    return switcher[world_size](plant)")
