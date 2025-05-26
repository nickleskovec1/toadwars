import Board
import Vehicle
from Enums import EUnitType
import random

weights_arr = []
x = 3
y = 3

for enum in [e.value for e in EUnitType.UnitType]:
    weights = []
    for i in range(y):
        arr = []
        for j in range(x):
            arr.append(random.randint(1, 4))
        weights.append(arr)
    weights_arr.append(weights)

board = Board.Board(weights_arr, None)
vehicle = Vehicle.Vehicle(0, 0, 5, 1, 3, 3, 20, EUnitType.UnitType.INFANTRY)
vehicle.check_move(board)

test = weights_arr[EUnitType.UnitType.INFANTRY.value]
for arr1 in test:
    print(arr1)
#print(weights_arr)

