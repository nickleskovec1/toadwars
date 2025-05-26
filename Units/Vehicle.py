from Board import Board
from Enums.EUnitType import UnitType

class Vehicle:

    def __init__(self, x, y, health, damage, range_min, range_max, movement, unit_type : UnitType):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.range_min = range_min
        self.range_max = range_max
        self.movement = movement
        self.unit_type = unit_type


    def gayAssRecursion(self, paths : dict, range, weights, current_path):
        if range > 0:
            y_pos = current_path[len(current_path)-1][0]
            x_pos = current_path[len(current_path)-1][1]
            nodes = []
            # check left node
            if x_pos > 0:
                x = x_pos - 1
                y = y_pos
                nodes.append((x,y))
            # check right node
            if x_pos < len(weights[y_pos]) - 1:
                x = x_pos + 1
                y = y_pos
                nodes.append((x,y))
            # check below node
            if y_pos < len(weights) - 1:
                x = x_pos
                y = y_pos + 1
                nodes.append((x,y))
            if y_pos > 0:
                x = x_pos
                y = y_pos - 1
                nodes.append((x,y))
            for node in nodes:
                new_path = []
                for element in current_path:
                    new_path.append(element)
                new_path.append(node)
                new_weight = range - weights[node[1]][node[0]]
                if new_weight >= 0:
                    if node not in paths:
                        paths[node] = {new_weight: new_path}
                    else:
                        old_weight = list(paths[node])[0]
                        if new_weight > old_weight:
                            paths[node] = {new_weight: new_path}
                    self.gayAssRecursion(paths, new_weight, weights, new_path)

    """
    give path to end position as well as the possible end positions
    
    """
    def check_move(self, board):
        available_pos = []
        weights = board.weights[self.unit_type.value]
        print(weights)
        paths = {}
        self.gayAssRecursion(paths, self.movement, weights, [(self.x, self.y)])
        print(paths)


    def move(self, x, y):
        print(x)
        #deltaX