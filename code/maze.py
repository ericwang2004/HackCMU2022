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
# comment
class Maze:
	def __init__(self, input_array, magic_graph):
		self.input_array = input_array
		self.cell_array = intArrayIntoCell(input_array)
		self.magic_graph = magic_graph # dictionary from ordered pairs to ordered pairs; only magic cells
	def get_cell_type(self, x, y, shiftx=0, shifty=0):
		return self.cell_array[x + shiftx][y + shifty].get_typ()

