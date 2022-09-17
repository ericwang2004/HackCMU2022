# cell.py

class Cell:
	def __init__(self, x, y, typ):
		'''
		x, y are coordinates
		typ represents the type of the cell
			0 = empty
			1 = wall
			2 = magic
		'''
		self.x = x
		self.y = y
		self.typ = typ
	def get_x(self):
		return self.x
	def get_y(self):
		return self.y
	def get_typ(self):
		return self.typ
