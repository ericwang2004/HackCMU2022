# cell.py
EMPTY = 0 
WALL = 1
MAGIC = 2

ASSETS = ['../asset/finger.jpeg', '../asset/finger.jpeg', '../asset/finger.jpeg']

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
	def draw(self, pixel_cord, display, asset_manager):
        #asset_path = ASSETS[self.typ]
		#if not asset_manager.contains_asset(asset_path):
		#	asset_manager.add_asset(asset_path, asset_path)
   
		#display.blit(asset_manager.retrieve(asset_path), (pixel_cord.x, pixel_cord.y))
		return
	def get_neighbors(x, y):
		return 
