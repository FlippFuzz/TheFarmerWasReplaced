from __builtins__ import Entities, Entity

B = Entities.Bush
C = Entities.Carrot
G = Entities.Grass
T = Entities.Tree
N = Entities.Grass  # N actually means empty, but easier to just be grass


def _plant_32_B() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (8, 0), (16, 0), (24, 0), (4, 4), (12, 4), (20, 4), (28, 4), (0, 8), (8, 8), (16, 8), (24, 8), (4, 12), (12, 12), (20, 12), (28, 12), (0, 16), (8, 16), (16, 16), (24, 16), (4, 20), (12, 20), (20, 20), (28, 20), (0, 24), (8, 24), (16, 24), (24, 24), (4, 28), (12, 28), (20, 28), (28, 28)], 
        [
            [B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, ], 
            [C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, ], 
            [C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, ], 
            [C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, ], 
            [C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, ], 
            [C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, ], 
            [C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, ], 
            [C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, N, C, G, T, B, C, G, T, ], 
            [C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, C, N, C, C, C, C, C, N, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
        ]
    )
    # fmt: on


def _plant_32_C() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (8, 0), (16, 0), (24, 0), (4, 4), (12, 4), (20, 4), (28, 4), (0, 8), (8, 8), (16, 8), (24, 8), (4, 12), (12, 12), (20, 12), (28, 12), (0, 16), (8, 16), (16, 16), (24, 16), (4, 20), (12, 20), (20, 20), (28, 20), (0, 24), (8, 24), (16, 24), (24, 24), (4, 28), (12, 28), (20, 28), (28, 28)], 
        [
            [C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, N, B, G, T, C, B, G, T, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
        ]
    )
    # fmt: on


def _plant_32_G() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (8, 0), (16, 0), (24, 0), (4, 4), (12, 4), (20, 4), (28, 4), (0, 8), (8, 8), (16, 8), (24, 8), (4, 12), (12, 12), (20, 12), (28, 12), (0, 16), (8, 16), (16, 16), (24, 16), (4, 20), (12, 20), (20, 20), (28, 20), (0, 24), (8, 24), (16, 24), (24, 24), (4, 28), (12, 28), (20, 28), (28, 28)], 
        [
            [G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
            [G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, ], 
            [N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, N, B, C, T, G, B, C, T, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, T, T, T, N, T, N, T, T, ], 
        ]
    )
    # fmt: on


def _plant_32_T() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (8, 0), (16, 0), (24, 0), (4, 4), (12, 4), (20, 4), (28, 4), (0, 8), (8, 8), (16, 8), (24, 8), (4, 12), (12, 12), (20, 12), (28, 12), (0, 16), (8, 16), (16, 16), (24, 16), (4, 20), (12, 20), (20, 20), (28, 20), (0, 24), (8, 24), (16, 24), (24, 24), (4, 28), (12, 28), (20, 28), (28, 28)], 
        [
            [T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, ], 
            [N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, ], 
            [T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, ], 
            [N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, ], 
            [T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, ], 
            [N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, ], 
            [T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, ], 
            [B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, ], 
            [N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, N, B, C, G, T, B, C, G, ], 
            [B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, C, C, N, C, ], 
            [G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, G, G, G, N, G, N, G, G, ], 
        ]
    )
    # fmt: on


def _plant_22_B() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (7, 1), (16, 1), (3, 4), (12, 4), (19, 5), (8, 7), (15, 8), (0, 9), (11, 11), (5, 12), (18, 12), (1, 15), (14, 15), (8, 16), (19, 18), (4, 19), (11, 20)], 
        [
            [B, C, G, T, T, T, T, T, T, T, G, G, G, N, T, T, T, T, T, C, G, T, ], 
            [C, C, C, C, C, G, T, B, C, G, T, T, C, C, G, T, B, C, G, T, C, C, ], 
            [G, G, G, G, G, C, C, C, C, C, N, G, G, G, C, C, C, C, C, C, N, G, ], 
            [T, T, T, T, T, T, G, G, G, N, T, T, T, T, T, G, G, G, G, G, G, N, ], 
            [C, G, T, B, C, G, T, T, C, C, G, T, B, C, G, T, T, T, T, T, T, T, ], 
            [T, C, C, C, C, C, N, G, G, G, C, C, C, C, C, C, C, G, T, B, C, G, ], 
            [C, N, G, G, G, N, T, T, T, T, T, G, G, G, G, G, G, C, C, C, C, C, ], 
            [G, G, N, T, N, C, G, T, B, C, G, T, T, T, T, T, T, T, G, G, G, G, ], 
            [T, T, T, N, N, N, C, C, C, C, C, C, C, G, T, B, C, G, T, T, T, T, ], 
            [B, C, G, T, N, C, N, G, G, G, G, G, G, C, C, C, C, C, C, C, G, T, ], 
            [C, C, C, N, G, G, G, N, T, T, T, T, T, T, G, G, G, G, G, G, C, C, ], 
            [G, G, N, T, T, T, T, T, C, G, T, B, C, G, T, T, T, T, T, T, T, G, ], 
            [T, C, C, G, T, B, C, G, T, C, C, C, C, C, C, C, G, T, B, C, G, T, ], 
            [G, G, G, C, C, C, C, C, C, N, G, G, G, G, G, G, C, C, C, C, C, N, ], 
            [T, T, T, T, G, G, G, G, G, G, N, T, T, T, T, T, T, G, G, G, N, T, ], 
            [T, B, C, G, T, T, T, T, T, T, T, C, G, T, B, C, G, T, T, C, C, G, ], 
            [C, C, C, C, C, C, G, T, B, C, G, T, C, C, C, C, C, N, G, G, G, C, ], 
            [G, G, G, G, G, G, C, C, C, C, C, C, N, G, G, G, N, T, T, T, T, T, ], 
            [T, T, T, T, T, T, T, G, G, G, G, G, G, N, T, N, C, G, T, B, C, G, ], 
            [C, C, G, T, B, C, G, T, T, T, T, T, T, T, N, N, N, C, C, C, C, C, ], 
            [G, G, C, C, C, C, C, C, C, G, T, B, C, G, T, N, C, N, G, G, G, G, ], 
            [T, T, T, G, G, G, G, G, G, C, C, C, C, C, N, G, G, G, N, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_22_C() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (7, 1), (16, 1), (3, 4), (12, 4), (19, 5), (8, 7), (15, 8), (0, 9), (11, 11), (5, 12), (18, 12), (1, 15), (14, 15), (8, 16), (19, 18), (4, 19), (11, 20)], 
        [
            [C, B, G, T, T, T, T, T, T, T, G, G, G, N, T, T, T, T, T, B, G, T, ], 
            [B, B, B, B, B, G, T, C, B, G, T, T, B, B, G, T, C, B, G, T, B, B, ], 
            [G, G, G, G, G, B, B, B, B, B, N, G, G, G, B, B, B, B, B, B, N, G, ], 
            [T, T, T, T, T, T, G, G, G, N, T, T, T, T, T, G, G, G, G, G, G, N, ], 
            [B, G, T, C, B, G, T, T, B, B, G, T, C, B, G, T, T, T, T, T, T, T, ], 
            [T, B, B, B, B, B, N, G, G, G, B, B, B, B, B, B, B, G, T, C, B, G, ], 
            [B, N, G, G, G, N, T, T, T, T, T, G, G, G, G, G, G, B, B, B, B, B, ], 
            [G, G, N, T, N, B, G, T, C, B, G, T, T, T, T, T, T, T, G, G, G, G, ], 
            [T, T, T, N, N, N, B, B, B, B, B, B, B, G, T, C, B, G, T, T, T, T, ], 
            [C, B, G, T, N, B, N, G, G, G, G, G, G, B, B, B, B, B, B, B, G, T, ], 
            [B, B, B, N, G, G, G, N, T, T, T, T, T, T, G, G, G, G, G, G, B, B, ], 
            [G, G, N, T, T, T, T, T, B, G, T, C, B, G, T, T, T, T, T, T, T, G, ], 
            [T, B, B, G, T, C, B, G, T, B, B, B, B, B, B, B, G, T, C, B, G, T, ], 
            [G, G, G, B, B, B, B, B, B, N, G, G, G, G, G, G, B, B, B, B, B, N, ], 
            [T, T, T, T, G, G, G, G, G, G, N, T, T, T, T, T, T, G, G, G, N, T, ], 
            [T, C, B, G, T, T, T, T, T, T, T, B, G, T, C, B, G, T, T, B, B, G, ], 
            [B, B, B, B, B, B, G, T, C, B, G, T, B, B, B, B, B, N, G, G, G, B, ], 
            [G, G, G, G, G, G, B, B, B, B, B, B, N, G, G, G, N, T, T, T, T, T, ], 
            [T, T, T, T, T, T, T, G, G, G, G, G, G, N, T, N, B, G, T, C, B, G, ], 
            [B, B, G, T, C, B, G, T, T, T, T, T, T, T, N, N, N, B, B, B, B, B, ], 
            [G, G, B, B, B, B, B, B, B, G, T, C, B, G, T, N, B, N, G, G, G, G, ], 
            [T, T, T, G, G, G, G, G, G, B, B, B, B, B, N, G, G, G, N, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_22_G() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (7, 1), (16, 1), (3, 4), (12, 4), (19, 5), (8, 7), (15, 8), (0, 9), (11, 11), (5, 12), (18, 12), (1, 15), (14, 15), (8, 16), (19, 18), (4, 19), (11, 20)], 
        [
            [G, B, C, T, T, T, T, T, T, T, C, C, C, N, T, T, T, T, T, B, C, T, ], 
            [B, B, B, B, B, C, T, G, B, C, T, T, B, B, C, T, G, B, C, T, B, B, ], 
            [C, C, C, C, C, B, B, B, B, B, N, C, C, C, B, B, B, B, B, B, N, C, ], 
            [T, T, T, T, T, T, C, C, C, N, T, T, T, T, T, C, C, C, C, C, C, N, ], 
            [B, C, T, G, B, C, T, T, B, B, C, T, G, B, C, T, T, T, T, T, T, T, ], 
            [T, B, B, B, B, B, N, C, C, C, B, B, B, B, B, B, B, C, T, G, B, C, ], 
            [B, N, C, C, C, N, T, T, T, T, T, C, C, C, C, C, C, B, B, B, B, B, ], 
            [C, C, N, T, N, B, C, T, G, B, C, T, T, T, T, T, T, T, C, C, C, C, ], 
            [T, T, T, N, N, N, B, B, B, B, B, B, B, C, T, G, B, C, T, T, T, T, ], 
            [G, B, C, T, N, B, N, C, C, C, C, C, C, B, B, B, B, B, B, B, C, T, ], 
            [B, B, B, N, C, C, C, N, T, T, T, T, T, T, C, C, C, C, C, C, B, B, ], 
            [C, C, N, T, T, T, T, T, B, C, T, G, B, C, T, T, T, T, T, T, T, C, ], 
            [T, B, B, C, T, G, B, C, T, B, B, B, B, B, B, B, C, T, G, B, C, T, ], 
            [C, C, C, B, B, B, B, B, B, N, C, C, C, C, C, C, B, B, B, B, B, N, ], 
            [T, T, T, T, C, C, C, C, C, C, N, T, T, T, T, T, T, C, C, C, N, T, ], 
            [T, G, B, C, T, T, T, T, T, T, T, B, C, T, G, B, C, T, T, B, B, C, ], 
            [B, B, B, B, B, B, C, T, G, B, C, T, B, B, B, B, B, N, C, C, C, B, ], 
            [C, C, C, C, C, C, B, B, B, B, B, B, N, C, C, C, N, T, T, T, T, T, ], 
            [T, T, T, T, T, T, T, C, C, C, C, C, C, N, T, N, B, C, T, G, B, C, ], 
            [B, B, C, T, G, B, C, T, T, T, T, T, T, T, N, N, N, B, B, B, B, B, ], 
            [C, C, B, B, B, B, B, B, B, C, T, G, B, C, T, N, B, N, C, C, C, C, ], 
            [T, T, T, C, C, C, C, C, C, B, B, B, B, B, N, C, C, C, N, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_22_T() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (7, 1), (16, 1), (3, 4), (12, 4), (19, 5), (8, 7), (15, 8), (0, 9), (11, 11), (5, 12), (18, 12), (1, 15), (14, 15), (8, 16), (19, 18), (4, 19), (11, 20)], 
        [
            [T, B, C, G, G, G, G, G, G, G, C, C, C, N, G, G, G, G, G, B, C, G, ], 
            [B, B, B, B, B, C, G, T, B, C, G, G, B, B, C, G, T, B, C, G, B, B, ], 
            [C, C, C, C, C, B, B, B, B, B, N, C, C, C, B, B, B, B, B, B, N, C, ], 
            [G, G, G, G, G, G, C, C, C, N, G, G, G, G, G, C, C, C, C, C, C, N, ], 
            [B, C, G, T, B, C, G, G, B, B, C, G, T, B, C, G, G, G, G, G, G, G, ], 
            [G, B, B, B, B, B, N, C, C, C, B, B, B, B, B, B, B, C, G, T, B, C, ], 
            [B, N, C, C, C, N, G, G, G, G, G, C, C, C, C, C, C, B, B, B, B, B, ], 
            [C, C, N, G, N, B, C, G, T, B, C, G, G, G, G, G, G, G, C, C, C, C, ], 
            [G, G, G, N, N, N, B, B, B, B, B, B, B, C, G, T, B, C, G, G, G, G, ], 
            [T, B, C, G, N, B, N, C, C, C, C, C, C, B, B, B, B, B, B, B, C, G, ], 
            [B, B, B, N, C, C, C, N, G, G, G, G, G, G, C, C, C, C, C, C, B, B, ], 
            [C, C, N, G, G, G, G, G, B, C, G, T, B, C, G, G, G, G, G, G, G, C, ], 
            [G, B, B, C, G, T, B, C, G, B, B, B, B, B, B, B, C, G, T, B, C, G, ], 
            [C, C, C, B, B, B, B, B, B, N, C, C, C, C, C, C, B, B, B, B, B, N, ], 
            [G, G, G, G, C, C, C, C, C, C, N, G, G, G, G, G, G, C, C, C, N, G, ], 
            [G, T, B, C, G, G, G, G, G, G, G, B, C, G, T, B, C, G, G, B, B, C, ], 
            [B, B, B, B, B, B, C, G, T, B, C, G, B, B, B, B, B, N, C, C, C, B, ], 
            [C, C, C, C, C, C, B, B, B, B, B, B, N, C, C, C, N, G, G, G, G, G, ], 
            [G, G, G, G, G, G, G, C, C, C, C, C, C, N, G, N, B, C, G, T, B, C, ], 
            [B, B, C, G, T, B, C, G, G, G, G, G, G, G, N, N, N, B, B, B, B, B, ], 
            [C, C, B, B, B, B, B, B, B, C, G, T, B, C, G, N, B, N, C, C, C, C, ], 
            [G, G, G, C, C, C, C, C, C, B, B, B, B, B, N, C, C, C, N, G, G, G, ], 
        ]
    )
    # fmt: on


def _plant_16_B() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (5, 3), (12, 3), (10, 8), (1, 9), (13, 12), (4, 13), (9, 15)], 
        [
            [B, C, G, T, T, C, N, C, C, C, C, C, C, C, G, T, ], 
            [C, C, C, N, G, G, G, N, G, G, G, G, G, G, C, C, ], 
            [G, G, N, T, T, T, T, T, N, T, T, T, T, T, T, G, ], 
            [T, N, C, G, T, B, C, G, T, C, G, T, B, C, G, T, ], 
            [N, N, N, C, C, C, C, C, N, N, C, C, C, C, C, N, ], 
            [N, N, N, N, G, G, G, N, N, N, C, G, G, G, N, N, ], 
            [N, C, N, N, N, T, N, N, N, G, G, G, T, N, N, N, ], 
            [G, G, G, N, N, N, N, N, T, T, T, T, T, N, N, N, ], 
            [T, T, T, T, N, N, N, C, G, T, B, C, G, T, N, T, ], 
            [T, B, C, G, T, N, N, N, C, C, C, C, C, C, C, G, ], 
            [C, C, C, C, C, N, N, N, N, G, G, G, G, G, G, C, ], 
            [G, G, G, G, G, G, N, N, N, N, T, T, T, T, T, T, ], 
            [T, T, T, T, T, T, T, N, N, C, C, G, T, B, C, G, ], 
            [C, C, G, T, B, C, G, T, G, G, G, C, C, C, C, C, ], 
            [G, G, C, C, C, C, C, T, T, T, T, T, G, G, G, G, ], 
            [T, T, T, G, G, G, C, G, T, B, C, G, T, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_16_C() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (5, 3), (12, 3), (10, 8), (1, 9), (13, 12), (4, 13), (9, 15)], 
        [
            [C, B, G, T, T, B, N, B, B, B, B, B, B, B, G, T, ], 
            [B, B, B, N, G, G, G, N, G, G, G, G, G, G, B, B, ], 
            [G, G, N, T, T, T, T, T, N, T, T, T, T, T, T, G, ], 
            [T, N, B, G, T, C, B, G, T, B, G, T, C, B, G, T, ], 
            [N, N, N, B, B, B, B, B, N, N, B, B, B, B, B, N, ], 
            [N, N, N, N, G, G, G, N, N, N, B, G, G, G, N, N, ], 
            [N, B, N, N, N, T, N, N, N, G, G, G, T, N, N, N, ], 
            [G, G, G, N, N, N, N, N, T, T, T, T, T, N, N, N, ], 
            [T, T, T, T, N, N, N, B, G, T, C, B, G, T, N, T, ], 
            [T, C, B, G, T, N, N, N, B, B, B, B, B, B, B, G, ], 
            [B, B, B, B, B, N, N, N, N, G, G, G, G, G, G, B, ], 
            [G, G, G, G, G, G, N, N, N, N, T, T, T, T, T, T, ], 
            [T, T, T, T, T, T, T, N, N, B, B, G, T, C, B, G, ], 
            [B, B, G, T, C, B, G, T, G, G, G, B, B, B, B, B, ], 
            [G, G, B, B, B, B, B, T, T, T, T, T, G, G, G, G, ], 
            [T, T, T, G, G, G, B, G, T, C, B, G, T, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_16_G() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (5, 3), (12, 3), (10, 8), (1, 9), (13, 12), (4, 13), (9, 15)], 
        [
            [G, B, C, T, T, B, N, B, B, B, B, B, B, B, C, T, ], 
            [B, B, B, N, C, C, C, N, C, C, C, C, C, C, B, B, ], 
            [C, C, N, T, T, T, T, T, N, T, T, T, T, T, T, C, ], 
            [T, N, B, C, T, G, B, C, T, B, C, T, G, B, C, T, ], 
            [N, N, N, B, B, B, B, B, N, N, B, B, B, B, B, N, ], 
            [N, N, N, N, C, C, C, N, N, N, B, C, C, C, N, N, ], 
            [N, B, N, N, N, T, N, N, N, C, C, C, T, N, N, N, ], 
            [C, C, C, N, N, N, N, N, T, T, T, T, T, N, N, N, ], 
            [T, T, T, T, N, N, N, B, C, T, G, B, C, T, N, T, ], 
            [T, G, B, C, T, N, N, N, B, B, B, B, B, B, B, C, ], 
            [B, B, B, B, B, N, N, N, N, C, C, C, C, C, C, B, ], 
            [C, C, C, C, C, C, N, N, N, N, T, T, T, T, T, T, ], 
            [T, T, T, T, T, T, T, N, N, B, B, C, T, G, B, C, ], 
            [B, B, C, T, G, B, C, T, C, C, C, B, B, B, B, B, ], 
            [C, C, B, B, B, B, B, T, T, T, T, T, C, C, C, C, ], 
            [T, T, T, C, C, C, B, C, T, G, B, C, T, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_16_T() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (5, 3), (12, 3), (10, 8), (1, 9), (13, 12), (4, 13), (9, 15)], 
        [
            [T, B, C, G, G, B, N, B, B, B, B, B, B, B, C, G, ], 
            [B, B, B, N, C, C, C, N, C, C, C, C, C, C, B, B, ], 
            [C, C, N, G, G, G, G, G, N, G, G, G, G, G, G, C, ], 
            [G, N, B, C, G, T, B, C, G, B, C, G, T, B, C, G, ], 
            [N, N, N, B, B, B, B, B, N, N, B, B, B, B, B, N, ], 
            [N, N, N, N, C, C, C, N, N, N, B, C, C, C, N, N, ], 
            [N, B, N, N, N, G, N, N, N, C, C, C, G, N, N, N, ], 
            [C, C, C, N, N, N, N, N, G, G, G, G, G, N, N, N, ], 
            [G, G, G, G, N, N, N, B, C, G, T, B, C, G, N, G, ], 
            [G, T, B, C, G, N, N, N, B, B, B, B, B, B, B, C, ], 
            [B, B, B, B, B, N, N, N, N, C, C, C, C, C, C, B, ], 
            [C, C, C, C, C, C, N, N, N, N, G, G, G, G, G, G, ], 
            [G, G, G, G, G, G, G, N, N, B, B, C, G, T, B, C, ], 
            [B, B, C, G, T, B, C, G, C, C, C, B, B, B, B, B, ], 
            [C, C, B, B, B, B, B, G, G, G, G, G, C, C, C, C, ], 
            [G, G, G, C, C, C, B, C, G, T, B, C, G, G, G, G, ], 
        ]
    )
    # fmt: on


def _plant_12_B() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (8, 4), (2, 5), (6, 11)], 
        [
            [B, C, G, T, C, C, C, C, C, C, G, T, ], 
            [C, C, C, N, N, G, G, G, C, N, C, C, ], 
            [G, G, C, N, N, N, T, G, G, G, N, G, ], 
            [T, G, G, G, N, N, T, T, T, T, T, N, ], 
            [T, T, T, T, T, C, G, T, B, C, G, T, ], 
            [G, T, B, C, G, T, C, C, C, C, C, C, ], 
            [C, C, C, C, C, N, N, G, G, G, N, N, ], 
            [N, G, G, G, N, N, N, N, T, N, N, N, ], 
            [N, N, T, N, N, N, C, N, N, N, N, N, ], 
            [C, N, N, N, N, G, G, G, N, N, N, N, ], 
            [G, G, N, N, T, T, T, T, T, N, N, G, ], 
            [T, T, T, C, G, T, B, C, G, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_12_C() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (8, 4), (2, 5), (6, 11)], 
        [
            [C, B, G, T, B, B, B, B, B, B, G, T, ], 
            [B, B, B, N, N, G, G, G, B, N, B, B, ], 
            [G, G, B, N, N, N, T, G, G, G, N, G, ], 
            [T, G, G, G, N, N, T, T, T, T, T, N, ], 
            [T, T, T, T, T, B, G, T, C, B, G, T, ], 
            [G, T, C, B, G, T, B, B, B, B, B, B, ], 
            [B, B, B, B, B, N, N, G, G, G, N, N, ], 
            [N, G, G, G, N, N, N, N, T, N, N, N, ], 
            [N, N, T, N, N, N, B, N, N, N, N, N, ], 
            [B, N, N, N, N, G, G, G, N, N, N, N, ], 
            [G, G, N, N, T, T, T, T, T, N, N, G, ], 
            [T, T, T, B, G, T, C, B, G, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_12_G() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (8, 4), (2, 5), (6, 11)], 
        [
            [G, B, C, T, B, B, B, B, B, B, C, T, ], 
            [B, B, B, N, N, C, C, C, B, N, B, B, ], 
            [C, C, B, N, N, N, T, C, C, C, N, C, ], 
            [T, C, C, C, N, N, T, T, T, T, T, N, ], 
            [T, T, T, T, T, B, C, T, G, B, C, T, ], 
            [C, T, G, B, C, T, B, B, B, B, B, B, ], 
            [B, B, B, B, B, N, N, C, C, C, N, N, ], 
            [N, C, C, C, N, N, N, N, T, N, N, N, ], 
            [N, N, T, N, N, N, B, N, N, N, N, N, ], 
            [B, N, N, N, N, C, C, C, N, N, N, N, ], 
            [C, C, N, N, T, T, T, T, T, N, N, C, ], 
            [T, T, T, B, C, T, G, B, C, T, T, T, ], 
        ]
    )
    # fmt: on


def _plant_12_T() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (8, 4), (2, 5), (6, 11)], 
        [
            [T, B, C, G, B, B, B, B, B, B, C, G, ], 
            [B, B, B, N, N, C, C, C, B, N, B, B, ], 
            [C, C, B, N, N, N, G, C, C, C, N, C, ], 
            [G, C, C, C, N, N, G, G, G, G, G, N, ], 
            [G, G, G, G, G, B, C, G, T, B, C, G, ], 
            [C, G, T, B, C, G, B, B, B, B, B, B, ], 
            [B, B, B, B, B, N, N, C, C, C, N, N, ], 
            [N, C, C, C, N, N, N, N, G, N, N, N, ], 
            [N, N, G, N, N, N, B, N, N, N, N, N, ], 
            [B, N, N, N, N, C, C, C, N, N, N, N, ], 
            [C, C, N, N, G, G, G, G, G, N, N, C, ], 
            [G, G, G, B, C, G, T, B, C, G, G, G, ], 
        ]
    )
    # fmt: on


def _plant_8_B() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (4, 4)], 
        [
            [B, C, G, T, N, C, G, T, ], 
            [C, C, C, N, C, N, C, C, ], 
            [G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, ], 
            [N, C, G, T, B, C, G, T, ], 
            [C, N, C, C, C, C, C, N, ], 
            [G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, ], 
        ]
    )
    # fmt: on


def _plant_8_C() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (4, 4)], 
        [
            [C, B, G, T, N, B, G, T, ], 
            [B, B, B, N, B, N, B, B, ], 
            [G, G, N, G, G, G, N, G, ], 
            [T, N, T, T, T, T, T, N, ], 
            [N, B, G, T, C, B, G, T, ], 
            [B, N, B, B, B, B, B, N, ], 
            [G, G, N, G, G, G, N, G, ], 
            [T, T, T, N, T, N, T, T, ], 
        ]
    )
    # fmt: on


def _plant_8_G() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (4, 4)], 
        [
            [G, B, C, T, N, B, C, T, ], 
            [B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, ], 
            [T, N, T, T, T, T, T, N, ], 
            [N, B, C, T, G, B, C, T, ], 
            [B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, ], 
            [T, T, T, N, T, N, T, T, ], 
        ]
    )
    # fmt: on


def _plant_8_T() -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    # fmt: off
    return (
        [(0, 0), (4, 4)], 
        [
            [T, B, C, G, N, B, C, G, ], 
            [B, B, B, N, B, N, B, B, ], 
            [C, C, N, C, C, C, N, C, ], 
            [G, N, G, G, G, G, G, N, ], 
            [N, B, C, G, T, B, C, G, ], 
            [B, N, B, B, B, B, B, N, ], 
            [C, C, N, C, C, C, N, C, ], 
            [G, G, G, N, G, N, G, G, ], 
        ]
    )
    # fmt: on


def _plant_32(plant: Entity) -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    switcher = {B: _plant_32_B, C: _plant_32_C, G: _plant_32_G, T: _plant_32_T}
    return switcher[plant]()


def _plant_22(plant: Entity) -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    switcher = {B: _plant_22_B, C: _plant_22_C, G: _plant_22_G, T: _plant_22_T}
    return switcher[plant]()


def _plant_16(plant: Entity) -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    switcher = {B: _plant_16_B, C: _plant_16_C, G: _plant_16_G, T: _plant_16_T}
    return switcher[plant]()


def _plant_12(plant: Entity) -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    switcher = {B: _plant_12_B, C: _plant_12_C, G: _plant_12_G, T: _plant_12_T}
    return switcher[plant]()


def _plant_8(plant: Entity) -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    switcher = {B: _plant_8_B, C: _plant_8_C, G: _plant_8_G, T: _plant_8_T}
    return switcher[plant]()


def poly_pattern(
    plant: Entity, world_size: int
) -> tuple[list[tuple[int, int]], list[list[Entity]]]:
    switcher = {32: _plant_32, 22: _plant_22, 16: _plant_16, 12: _plant_12, 8: _plant_8}
    return switcher[world_size](plant)
