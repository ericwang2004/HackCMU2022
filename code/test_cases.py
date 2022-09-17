# contains test cases
import maze
from maze import Maze
from player import Player
import camera
from camera import Camera

input_array1 = [[1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]]

input_array2 = [[1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]]

maze = Maze(input_array1)
camera = Camera(3, 1)
player = Player(2, 2, "n", maze, camera)
print(player.view())