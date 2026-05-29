from __builtins__ import Direction, East, North, South, West

N = North
S = South
E = East
W = West


def get_map_8() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def get_map_16() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def get_map_32() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on
