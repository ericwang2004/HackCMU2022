# player.py

class Player:
	def __init__(self, x0, y0, dir0, maze):
		# x0, y0 are the initial coordinates of the player
		# dir0 is the initial orientation of the player {"n", "s", "e", "w"}
		self.x = x0
		self.y = y0
		self.dir = dir0
		self.maze = maze # stores the maze representation in which the player is placed

	# this is the only movement function that modifies the position of the player, respecting orientation
	def forward(self):
		newx = self.x
		newy = self.y
		# no change is made to the player's orientation
		if self.dir == "n": # determine the *potential* new position (obviously, if it's a wall, we can't go there)
			newy += 1
		elif self.dir == "s":
			newy -= 1
		elif self.dir == "e":
			newx += 1
		else: # orientation is "w"
			newx -= 1
		# update player's position depending on the nature of the cell about to be entered
		cell_type = self.maze.get_cell_type(x, y)
		if cell_type == 1: # if the cell type is a wall, keep x and y the same since we can't run into a wall
			return
		elif cell_type == 0: # if the cell is empty, enter it by updating x and y to the new coordinates
			self.x = newx
			self.y = newy
			return
		else: # if the cell is magic, teleport the player to the cell linked to this one TODO
			self.x = newx 
			self.y = newy
			return
	# the other two movement functions (left and right) only modify the orientation of the player
	# only forward modifies the position, as mentioned above
	# note: turning backwards can be achieved by two lefts or two rights composed
	def left(self):
		if self.dir == "n":
			self.dir = "w"
		elif self.dir == "s":
			self.dir = "e"
		elif self.dir == "e":
			self.dir = "n"
		else: # self.dir == "w"
			self.dir = "s"
		return
	def right(self):
		if self.dir == "n":
			self.dir = "e"
		elif self.dir == "e":
			self.dir = "s"
		elif self.dir == "s":
			self.dir = "w"
		else: # self.dir == "w"
			self.dir = "n"
		return

	def view(self):