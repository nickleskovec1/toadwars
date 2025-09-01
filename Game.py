import random
import math

import pyglet
from pyglet import shapes
from pyglet.window import mouse

import Board
from Camera import Camera
from Enums import EUnitType
from Enums.ECameraMovementTypes import ECameraMovementTypes
from Enums.ETerrainType import ETerrainType
from Enums.ELayer import ELayer
from Units import Vehicle

GRID_X_PIXELS = 64  # num of horizontal pixels per tile
GRID_Y_PIXELS = 64  # num of vertical pixels per tile

window = pyglet.window.Window(fullscreen=False)
window.set_size(1300, 670)
SCREEN_WIDTH = window.width
SCREEN_HEIGHT = window.height
GRID_X_NUM_TILES = 30
GRID_Y_NUM_TILES = 30
#window.set_size(SCREEN_WIDTH, SCREEN_HEIGHT)
# image_map = pyglet.image.load('tile_map.jpg')
# sprites = []
# x = 25
# y = 85
# for i in range(6):
#     x = 25
#     for j in range(4):
#         region = image_map.get_region(x, y, 64, 64)
#         print(image_map)
#         sprites.append(pyglet.sprite.Sprite(region, x=j*64, y=i*64))
#         x += 64 + 9
#     y += 64 + 9
# #ball = pyglet.sprite.Sprite(ball_image, x=50, y=50)
#
# print(sprites[0])

sprite = pyglet.sprite.Sprite(pyglet.image.load('images/Grass_1.png'))


"""
Quick mental thoughts 
- have one batch
- have one group for each layer for that batch which priority matches layer level
- use sprite visibility for sprites that are either on screen or off screen (this optimizes the batch.draw call)
"""
batch = pyglet.graphics.Batch()
layers = []
for i in range(len([e.value for e in ELayer])):
    layers.append(pyglet.graphics.Group(order=i))

weights_arr = []
terrains = []
terrain_sprites = []
img = pyglet.image.load('images/Ground_1.png')
for i in range(GRID_X_NUM_TILES * GRID_Y_NUM_TILES):
    terrains.append(ETerrainType.FLATLAND)
    terrain_sprites.append( pyglet.sprite.Sprite(img,
                                   batch=batch, group=layers[ELayer.TERRAIN_LAYER.value], x=0, y=0))
x = GRID_X_NUM_TILES
y = GRID_Y_NUM_TILES
for enum in [e.value for e in EUnitType.UnitType]:
    weights = []
    for i in range(y):
        arr = []
        for j in range(x):
            arr.append(random.randint(1, 1))
        weights.append(arr)
    weights_arr.append(weights)

#tank_sprite = pyglet.sprite.Sprite(pyglet.image.load('images/T-34/ww2_top_view_hull4.png'),
#                                   batch=batch, group=layers[ELayer.SPRITE_LAYER.value])
board = Board.Board(weights_arr, terrains, terrain_sprites, GRID_X_NUM_TILES, GRID_Y_NUM_TILES)

for i in range(10):
    tank_sprite = pyglet.sprite.Sprite(pyglet.image.load('images/T-34/ww2_top_view_hull4.png'),
                                       batch=batch, group=layers[ELayer.SPRITE_LAYER.value], x=0, y=0)
    y = (800 + i) // GRID_X_NUM_TILES
    x = (800 + i) % GRID_X_NUM_TILES
    vehicle = Vehicle.Vehicle(x, y, 5, 1, 3, 3, 3, EUnitType.UnitType.INFANTRY, tank_sprite)
    board.board_units[800+i] = vehicle

print(len(layers))
print(ELayer.SPRITE_LAYER3.value)
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0,
                 0, 0, SCREEN_WIDTH/GRID_X_PIXELS, SCREEN_HEIGHT/GRID_Y_PIXELS,
                board, shapes.Box(0, 0, GRID_X_PIXELS, GRID_Y_PIXELS,
                                thickness=3, color=(255, 255, 255), batch=batch, group=layers[ELayer.SPRITE_LAYER2.value]),
                shapes.Box(0, 0, GRID_X_PIXELS, GRID_Y_PIXELS, thickness=3, color=(0,255,0),
                           batch=batch, group=layers[ELayer.SPRITE_LAYER3.value]))


@window.event
def on_mouse_press(x, y, button, modifiers):
    x_pos = (int)(camera.x_pos + x / GRID_X_PIXELS)
    y_pos = (int)((camera.y - y) // 64) + 1
    print(x_pos, y_pos)
    array_idx = y_pos * GRID_X_NUM_TILES + x_pos
    if array_idx in board.board_units:
        camera.selected = True
        board.board_units[array_idx].check_move(board)
        print("CHECKING MOVEMENT")
        camera.select_square.visible = True
        camera.selected_idx = array_idx
        camera.select_square.x = (camera.last_x + camera.x) // 64 * 64 - camera.x
        camera.select_square.y = (camera.last_y - camera.y) // 64 * 64 + camera.y
        #board.board_units[array_idx]
        print(board.board_units[array_idx])
    else:
        if camera.selected is True:
            print(board.board_units[camera.selected_idx].possible_moves)
            print(x_pos, y_pos)
            if (x_pos, y_pos) in board.board_units[camera.selected_idx].possible_moves:
                board.board_units[camera.selected_idx].move(x_pos, y_pos)
                board.board_units[array_idx] = board.board_units[camera.selected_idx]
                board.board_units.pop(camera.selected_idx)
                camera.select_square.visible = False
                camera.selected = False
    #print(x, y, x_pos, y_pos, camera.y_pos)

@window.event
def on_mouse_motion(x, y, dx, dy):
    camera.last_x = x
    camera.last_y = y
    CONDITION_NUM_EDGE_PIXELS = 100
    neg_y_cond = abs(y-SCREEN_HEIGHT) < CONDITION_NUM_EDGE_PIXELS
    neg_y_movement = (CONDITION_NUM_EDGE_PIXELS - abs(y-SCREEN_HEIGHT)) / CONDITION_NUM_EDGE_PIXELS
    pos_x_cond = abs(x-SCREEN_WIDTH) < CONDITION_NUM_EDGE_PIXELS
    pos_x_movement = (CONDITION_NUM_EDGE_PIXELS - abs(x-SCREEN_WIDTH)) / CONDITION_NUM_EDGE_PIXELS
    pos_y_cond = abs(y-SCREEN_HEIGHT) > (SCREEN_HEIGHT - CONDITION_NUM_EDGE_PIXELS)
    pos_y_movement = (abs(y-SCREEN_HEIGHT) - (SCREEN_HEIGHT - CONDITION_NUM_EDGE_PIXELS)) / CONDITION_NUM_EDGE_PIXELS
    neg_x_cond = abs(x - SCREEN_WIDTH) > (SCREEN_WIDTH-CONDITION_NUM_EDGE_PIXELS)
    neg_x_movement = (abs(x - SCREEN_WIDTH) - (SCREEN_WIDTH-CONDITION_NUM_EDGE_PIXELS)) / CONDITION_NUM_EDGE_PIXELS

    if pos_x_cond and pos_y_cond:
        camera.set_movement(ECameraMovementTypes.POS_XY, pos_x_movement, pos_y_movement)
    elif neg_x_cond and neg_y_cond:
        camera.movement_direction = ECameraMovementTypes.NEG_XY
        camera.set_movement(ECameraMovementTypes.NEG_XY, neg_x_movement, neg_y_movement)
    elif pos_x_cond and neg_y_cond:
        camera.set_movement(ECameraMovementTypes.POS_X_NEG_Y, pos_x_movement, neg_y_movement)
    elif neg_x_cond and pos_y_cond:
        camera.set_movement(ECameraMovementTypes.NEG_X_POS_Y, neg_x_movement, pos_y_movement)
    elif pos_x_cond:
        camera.set_movement(ECameraMovementTypes.POS_X, pos_x_movement, 0)
    elif neg_x_cond:
        camera.set_movement(ECameraMovementTypes.NEG_X, neg_x_movement, 0)
    elif pos_y_cond:
        camera.set_movement(ECameraMovementTypes.POS_Y, 0, pos_y_movement)
    elif neg_y_cond:
        camera.set_movement(ECameraMovementTypes.NEG_Y, 0, neg_y_movement)
        camera.movement_direction = ECameraMovementTypes.NEG_Y
    else:
        camera.set_movement(ECameraMovementTypes.NONE, 0, 0)

camera.draw()
camera.y = GRID_Y_PIXELS * (GRID_Y_NUM_TILES - 1)

@window.event
def on_draw():
    window.clear()
    camera.draw()
    batch.draw()

#
# def DEBUG_RESET_ALL_MOVEMENT():
#     for idx in board.board_units:
#         board.board_units[idx]

pyglet.app.run()