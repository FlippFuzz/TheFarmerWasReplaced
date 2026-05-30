from __builtins__ import Direction, East, North, South, West

N = North
S = South
E = East
W = West


def _get_map_4() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, N, ], 
        [S, N, W, W, ], 
        [S, E, E, N, ], 
        [S, W, W, W, ], 
    ]
    # fmt: on


def _get_map_6() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, ], 
        [S, E, E, E, E, N, ], 
        [S, N, W, W, W, W, ], 
        [S, E, E, E, E, N, ], 
        [S, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_8() -> list[list[Direction]]:
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


def _get_map_10() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_12() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_14() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_16() -> list[list[Direction]]:
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


def _get_map_18() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_20() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_22() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_24() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_26() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_28() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_30() -> list[list[Direction]]:
    # fmt: off
    return [
        [E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, N, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
        [S, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, E, N, ], 
        [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, ], 
    ]
    # fmt: on


def _get_map_32() -> list[list[Direction]]:
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


def get_map(world_size: int) -> list[list[Direction]]:
    switcher = {
        4: _get_map_4,
        6: _get_map_6,
        8: _get_map_8,
        10: _get_map_10,
        12: _get_map_12,
        14: _get_map_14,
        16: _get_map_16,
        18: _get_map_18,
        20: _get_map_20,
        22: _get_map_22,
        24: _get_map_24,
        26: _get_map_26,
        28: _get_map_28,
        30: _get_map_30,
        32: _get_map_32,
    }
    return switcher[world_size]()
