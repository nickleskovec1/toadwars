from Enums import ETerrainType

class Board:

    """
    weights: [EUnitType][y][x]] -> weights for moving to space for each unit type
    """
    def __init__(self, weights, terrain : ETerrainType):
        self.weights = weights
        self.terrain = terrain
