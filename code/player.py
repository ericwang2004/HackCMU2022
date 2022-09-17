# player.py

from animator import Animator
from maze import Maze
import pygame

DIRECTION_TO_ANIMATION = {'n': 3, 's': 0, 'e': 2, 'w': 1}

class Player:
    def __init__(self, x0, y0, dir0, maze, camera_length, asset_manager, endx, endy):
        # x0, y0 are the initial coordinates of the player
        # dir0 is the initial orientation of the player {"n", "s", "e", "w"}
        self.x = x0
        self.y = y0
        self.dir = dir0
        self.maze = maze # stores the maze representation in which the player is placed
        self.clength = camera_length # view looks like a square
        self.cx = self.x - self.clength // 2
        self.cy = self.y - self.clength // 2
				self.endx = endx
				self.endy = endy

        sprite_sheet = asset_manager.retrieve('./asset/aubreySheet.png')
        self.animator = Animator(sprite_sheet, 4, 3, 100)

    def draw(self, display, dimensions):
        frame = pygame.transform.scale(self.animator.get_frame(), dimensions)
        display.blit(frame, (2 * dimensions[0], 2 * dimensions[1]))
     
    def update(self, delta):	
        self.animator.current_animation = DIRECTION_TO_ANIMATION[self.dir]			
        self.animator.update(delta)
        
    def update_corner(self):
        # update self.cx and self.cy
				if self.x == self.endx and self.y == self.endy:
						return -1
        self.cx = self.x - self.clength // 2
        self.cy = self.y - self.clength // 2
        return 0
    # this is the only movement function that modifies the position of the player, respecting orientation
    def forward(self):
        newx = self.x
        newy = self.y
        # no change is made to the player's orientation
        newx -= 1
        self.dir = 'n'
        # update player's position depending on the nature of the cell about to be entered
        cell_type = self.maze.get_cell_type(newx, newy)
        if cell_type == 0: # if the cell is empty, enter it by updating x and y to the new coordinates
            self.x = newx
            self.y = newy
        elif cell_type == 2: # if the cell is magic, teleport the player to the cell linked to this one TODO
            self.x, self.y = self.maze.magic_graph[(newx, newy)]
        # if the cell type is a wall, keep x and y the same since we can't run into a wall
        return self.update_corner()
    # the other two movement functions (left and right) only modify the orientation of the player
    # only forward modifies the position, as mentioned above
    # note: turning backwards can be achieved by two lefts or two rights composed
    def left(self):
        newx = self.x
        newy = self.y
        # no change is made to the player's orientation
        newy -= 1
        self.dir = 'w'
        # update player's position depending on the nature of the cell about to be entered
        cell_type = self.maze.get_cell_type(newx, newy)
        if cell_type == 0: # if the cell is empty, enter it by updating x and y to the new coordinates
            self.x = newx
            self.y = newy
        elif cell_type == 2: # if the cell is magic, teleport the player to the cell linked to this one TODO
            self.x, self.y = self.maze.magic_graph[(newx, newy)]
        # if the cell type is a wall, keep x and y the same since we can't run into a wall
				return self.update_corner()
    def right(self):
        newx = self.x
        newy = self.y
        # no change is made to the player's orientation
        newy += 1
        self.dir = 'e'
        # update player's position depending on the nature of the cell about to be entered
        cell_type = self.maze.get_cell_type(newx, newy)
        if cell_type == 0: # if the cell is empty, enter it by updating x and y to the new coordinates
            self.x = newx
            self.y = newy
        elif cell_type == 2: # if the cell is magic, teleport the player to the cell linked to this one TODO
            self.x, self.y = self.maze.magic_graph[(newx, newy)]
        # if the cell type is a wall, keep x and y the same since we can't run into a wall
        return self.update_corner()
    def back(self):
        newx = self.x
        newy = self.y
        # no change is made to the player's orientation
        newx += 1
        self.dir = 's'
        # update player's position depending on the nature of the cell about to be entered
        cell_type = self.maze.get_cell_type(newx, newy)
        if cell_type == 0: # if the cell is empty, enter it by updating x and y to the new coordinates
            self.x = newx
            self.y = newy
        elif cell_type == 2: # if the cell is magic, teleport the player to the cell linked to this one TODO
            self.x, self.y = self.maze.magic_graph[(newx, newy)]
        # if the cell type is a wall, keep x and y the same since we can't run into a wall
        return self.update_corner()

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
                in_view_0.append((x, playerY)) 
                break 
        for x in range(playerX + 1, self.clength):
            if self.maze.get_cell_type(x, playerY, self.cx, self.cy) != 1:
                in_view_0.append((x, playerY)) 
            else:
                in_view_0.append((x, playerY)) 
                break 
        for y in range(playerY - 1, -1, -1):
            if self.maze.get_cell_type(playerX, y, self.cx, self.cy) != 1:
                in_view_0.append((playerX, y)) 
            else:
                in_view_0.append((playerX, y)) 
                break 
        for y in range(playerY + 1, self.clength):
            if self.maze.get_cell_type(playerX, y, self.cx, self.cy) != 1:
                in_view_0.append((playerX, y)) 
            else:
                in_view_0.append((playerX, y)) 
                break  
        
        # step 2: lighting (one iteration of flood fill)
        for x, y in in_view_0:
            in_view_1.add((x, y))
            if self.maze.get_cell_type(x, y, self.cx, self.cy) != 1:
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

    def __repr__(self):
        output = "({}, {}) {}\n".format(str(self.x), str(self.y), self.dir)
        viewarr = self.view()
        for row in viewarr:
            for cell in row:
                output += str(cell)
            output += "\n"
        return output
