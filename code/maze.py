# implement maze
from cell import Cell

def intArrayIntoCell(input_array):
    rows, cols = len(input_array), len(input_array[0])
    # create empty cell array of same dimensions
    cell_array = []
    for row in range(rows):
        cell_array.append([0] * cols)

    # fill cell array with cell objects
    for i in range(rows):
        for j in range(cols):
            cell_array[i][j] = Cell(i, j, input_array[i][j])
    return cell_array

class Maze:
    def __init__(self, x_max, y_max, input_array):
        self.x_max = x_max
        self.y_max = y_max
        self.input_array = input_array
        self.cell_array = intArrayIntoCell(input_array)
    
    def get_cell_type(self, x, y, input_array):
        return self.cell_array[x][y].typ

