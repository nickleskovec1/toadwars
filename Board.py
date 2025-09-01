import pyglet

from Enums import ETerrainType

class Board:

    """
    weights: [EUnitType][y][x]] -> weights for moving to space for each unit type
    """
    def __init__(self, weights, terrains: ETerrainType,
                 terrain_sprites: [pyglet.sprite.Sprite],
                 terrain_highlights: [pyglet.shapes.Box],
                 terrain_arrows: [pyglet.sprite.Sprite],
                 board_width, board_height):
        self.weights = weights
        self.terrains = terrains
        self.board_width = board_width
        self.board_height = board_height
        self.terrain_sprites = terrain_sprites
        self.terrain_highlights = terrain_highlights
        self.terrain_arrows = terrain_arrows
        self.board_units = {}

