from enum import Enum


class ECameraMovementTypes(Enum):
    NONE = 0
    POS_Y = 1
    NEG_Y = 2
    POS_X = 3
    NEG_X = 4
    POS_XY = 5
    NEG_XY = 6
    POS_X_NEG_Y = 7
    NEG_X_POS_Y = 8
