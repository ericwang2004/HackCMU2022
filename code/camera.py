
from vector import Vector

TILE_CAMERA_WIDTH = 3

class Camera:
    def __init__(self, tile_height, tile_pixel_dimensions) -> None:
        self.tile_height = tile_height
        self.tile_pixel_dimensions = tile_pixel_dimensions
        self.pos = Vector(0, 0)
        
    def get_screen_dimensions(self):
        return (TILE_CAMERA_WIDTH * self.tile_pixel_dimensions, self.tile_height * self.tile_pixel_dimensions)
    
    def center(self, new_pos):
        #camera position is the top left of the camera, (0, 0)
        #new_pos is what we want the center of the camera to be
        self.pos = new_pos.sub(Vector(TILE_CAMERA_WIDTH / 2.0, self.tile_height / 2.0))