import pyglet

from Enums.EUnitType import UnitType


class Unit:
    def __init__(self, x, y, health, damage, range_min,
                 range_max, movement, unit_type: UnitType,
                 a_sprite: pyglet.sprite.Sprite):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.range_min = range_min
        self.range_max = range_max
        self.movement = movement
        self.unit_type = unit_type
        self.m_sprite = a_sprite

    def __repr__(self):
        return "X: " + str(self.x) + " Y: " + str(self.y)