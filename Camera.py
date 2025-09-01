import math

from pyglet import shapes

from Board import Board
from Enums.ECameraMovementTypes import ECameraMovementTypes


class Camera:

    """
    screen_width - num total screen horizontal pixels (Camera captures full screen)
    screen_height - num total screen vertical pixels (Camera captures full screen)
    x_pos - top left board position of camera (horizontal)
    y_pos - top left board position of camera (vertical)
    x - float of camera's current horizontal position
    y - float of camera's current vertical
    range_x - how many board positions to the right of 'x(param)' can we see
    range_y - how many board positions below 'y(param)' can we see
    """
    def __init__(self, screen_width, screen_height, x, y,
                 x_pos, y_pos, range_x, range_y, board: Board,
                 hightlight_rectangle: shapes.Box,
                 select_rectangle: shapes.Box):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = x
        self.y = y
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.range_x = range_x
        self.range_y = range_y
        self.board = board
        self.movement_direction = ECameraMovementTypes.NONE
        self.CAMERA_MOVE_SPEED = 10
        self.highlight_square = hightlight_rectangle
        self.select_square = select_rectangle
        self.select_square.visible = False
        self.selected_idx = -1
        self.dx = 1
        self.dy = 1
        self.last_x = 0
        self.last_y = 0
        self.selected = False

    def move(self, x, y):
        self.x = x
        self.y = y

    def set_movement(self, movement_type: ECameraMovementTypes, dx: float, dy: float):
        self.movement_direction = movement_type
        self.dx = dx * self.CAMERA_MOVE_SPEED
        self.dy = dy * self.CAMERA_MOVE_SPEED

    def draw(self):
        if self.movement_direction == ECameraMovementTypes.POS_X:
            self.move(self.x+self.dx, self.y)
            self.select_square.x -= self.dx
        elif self.movement_direction == ECameraMovementTypes.NEG_X:
            self.move(self.x-self.dx, self.y)
            self.select_square.x += self.dx
        elif self.movement_direction == ECameraMovementTypes.POS_Y:
            self.move(self.x, self.y+self.dy)
            self.select_square.y += self.dy
        elif self.movement_direction == ECameraMovementTypes.NEG_Y:
            self.move(self.x, self.y-self.dy)
            self.select_square.y -= self.dy
        elif self.movement_direction == ECameraMovementTypes.POS_XY:
            self.move(self.x+self.dx, self.y+self.dy)
            self.select_square.y += self.dy
            self.select_square.x -= self.dx
        elif self.movement_direction == ECameraMovementTypes.POS_X_NEG_Y:
            self.move(self.x+self.dx, self.y-self.dy)
            self.select_square.y -= self.dy
            self.select_square.x -= self.dx
        elif self.movement_direction == ECameraMovementTypes.NEG_X_POS_Y:
            self.move(self.x-self.dx, self.y+self.dy)
            self.select_square.y += self.dy
            self.select_square.x += self.dx
        elif self.movement_direction == ECameraMovementTypes.NEG_XY:
            self.move(self.x-self.dx, self.y-self.dy)
            self.select_square.y -= self.dy
            self.select_square.x += self.dx

        self.x_pos = (self.x / self.screen_width) * self.range_x
        self.y_pos = (self.y / self.screen_height) * self.range_y
       # print(self.x_pos, self.y_pos)

        for i in range(len(self.board.terrain_sprites)):
            x_pos = i % self.board.board_width
            y_pos = i // self.board.board_height
            # TODO -> put logic in here about making sprite invisible so it doesn't always draw if offscreen
            # TODO -> almost 100% not required but cool code
            x_coord = (x_pos - self.x_pos) * self.screen_width / self.range_x
            y_coord =  (self.y_pos - y_pos) * self.screen_height / self.range_y

            #print(y_pos, y_coord)
            self.board.terrain_sprites[i].update(x=x_coord, y=y_coord)
            self.board.terrain_arrows[i].update(x=x_coord+32, y=y_coord+32)
            self.board.terrain_highlights[i].x = x_coord
            self.board.terrain_highlights[i].y = y_coord
            #self.board.terrain_highlights[i].update(x=x_coord, y=y_coord)
        for board_unit_pos in self.board.board_units:
            x_pos = board_unit_pos % self.board.board_width
            y_pos = board_unit_pos // self.board.board_height
            x_coord = (x_pos - self.x_pos) * self.screen_width / self.range_x
            y_coord = self.screen_height + (self.y_pos - y_pos) * self.screen_height / self.range_y
            y_coord = (self.y_pos - y_pos) * self.screen_height / self.range_y
            self.board.board_units[board_unit_pos].m_sprite.update(x=x_coord, y=y_coord)

        # if self.dx >= 0:
        #     self.select_square.x -= self.dx
        # if self.dy >= 0:
        #     self.select_square.y -= self.dy
        # else:
        #     self.select_square.y += self.dy
        #print(self.select_square.y, self.dy)



        self.highlight_square.x = (self.last_x + self.x) // 64 * 64 - self.x
        self.highlight_square.y = (self.last_y - self.y) // 64 * 64 + self.y

