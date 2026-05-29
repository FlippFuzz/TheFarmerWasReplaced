from builtins import str as str

N = "N"
S = "S"
E = "E"
W = "W"
X = "X"


def generate_map(world_size: int) -> list[list[str]]:
    # Map will be [y][x]
    map = [[X for _ in range(world_size)] for _ in range(world_size)]

    for y in range(world_size):
        for x in range(world_size):
            if x == 0:
                # Column 0 is the return path South to (0,0)
                map[y][x] = E if y == 0 else S
            elif y == 0:
                # Bottom row moves East and turns North at the edge
                map[y][x] = N if x == world_size - 1 else E
            elif y == world_size - 1:
                # Top row moves West back to the return column
                map[y][x] = W
            elif y % 2 == 1:
                # Odd rows snake West and turn North at column 1
                map[y][x] = N if x == 1 else W
            else:
                # Even rows snake East and turn North at the last column
                map[y][x] = N if x == world_size - 1 else E
    return map


if __name__ == "__main__":
    world_sizes = [8, 16, 32]

    print("from __builtins__ import North, South, East, West, Direction")
    print("")
    print("N = North")
    print("S = South")
    print("E = East")
    print("W = West")
    print("")
    print("")

    for world_size in world_sizes:
        map = generate_map(world_size)

        print(f"def get_map_{world_size}() -> list[list[Direction]]:")
        print("    # fmt: off")
        print("    return [")
        for row in map:
            row_str = "        ["
            for element in row:
                row_str += f"{element}, "
            print(row_str + "], ")
        print("    ]")
        print("    # fmt: on")
        print("")
        print("")
