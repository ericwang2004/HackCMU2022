# player.py

from maze import Maze

class Player:
	def __init__(self, x0, y0, dir0, maze, camera_length):
		# x0, y0 are the initial coordinates of the player
		# dir0 is the initial orientation of the player {"n", "s", "e", "w"}
		self.x = x0
		self.y = y0
		self.dir = dir0
		self.maze = maze # stores the maze representation in which the player is placed
		self.clength = camera_length # view looks like a square
		self.cx = self.x - self.clength // 2
		self.cy = self.y - self.clength // 2

	# this is the only movement function that modifies the position of the player, respecting orientation
	def forward(self):
		newx = self.x
		newy = self.y
		# no change is made to the player's orientation
		if self.dir == "n": # determine the *potential* new position (obviously, if it's a wall, we can't go there)
			newx -= 1
		elif self.dir == "s":
			newx += 1
		elif self.dir == "e":
			newy += 1
		else: # orientation is "w"
			newy -= 1
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
		# initialize array 
		# 0 = Empty
		# 1 = Wall
		# 2 = Magic
		# 3 = Invisible
		view_array = []
		rows, cols = self.clength, self.clength
		for row in range(rows):
			view_array.append([3]*cols)
		
		# start in player position
		# note: this is relative to the camera view subarray
		playerX, playerY = self.clength // 2, self.clength // 2
		view_array[playerX][playerY] = 0

		# step 1: shoot rays in all four directions
		in_view_0 = []
		in_view_1 = set()
		for x in range(playerX - 1, -1, -1):
			if self.maze.get_cell_type(x, playerY, self.cx, self.cy) != 1:
				in_view_0.append((x, playerY)) 
			else:
				break 
		for x in range(playerX + 1, self.clength):
			if self.maze.get_cell_type(x, playerY, self.cx, self.cy) != 1:
				in_view_0.append((x, playerY)) 
			else:
				break 
		for y in range(playerY - 1, -1, -1):
			if self.maze.get_cell_type(playerX, y, self.cx, self.cy) != 1:
				in_view_0.append((playerX, y)) 
			else:
				break 
		for y in range(playerY + 1, self.clength):
			if self.maze.get_cell_type(playerX, y, self.cx, self.cy) != 1:
				in_view_0.append((playerX, y)) 
			else:
				break  
		
		# step 2: lighting
		for x, y in in_view_0:
			in_view_1.add((x, y))
			if x + 1 < self.clength:
				in_view_1.add((x + 1, y))
			if x - 1 >= 0:
				in_view_1.add((x - 1, y))
			if y + 1 < self.clength:
				in_view_1.add((x, y + 1))
			if y - 1 >= 0:
				in_view_1.add((x, y - 1))

		# update view array
		for x, y in in_view_1:
			view_array[x][y] = self.maze.get_cell_type(x, y, self.cx, self.cy)
		return view_array


