
from vector import Vector
TILE_CAMERA_WIDTH = 3

def clamp(val, min_, max_):
    return max(min_, min(val, max_))

class Camera:
    def __init__(self, tile_camera_height, tile_pixel_dimensions) -> None:
        self.tile_camera_height = tile_camera_height
        self.tile_pixel_dimensions = tile_pixel_dimensions
        self.pos = Vector(0, 0)
        
    def get_screen_dimensions(self):
        return (TILE_CAMERA_WIDTH * self.tile_pixel_dimensions, self.tile_camera_height * self.tile_pixel_dimensions)
    
    def center(self, player_pos, map_max_x, map_max_y):
        #camera position is the top left of the camera, (0, 0)
        #new_pos is what we want the center of the camera to be
        self.pos.y = player_pos.y - self.tile_camera_height / 2.0
        
        #Get the clamped integer coordinate (tile coordinate) of the player's x position, then add half a tile to it
        #Center ourselves onto that by subtracting the cam width / 2
        self.pos.x = (int(player_pos.x) + 0.5) - TILE_CAMERA_WIDTH / 2.0
        
        #Next clamp the camera such that it doesn't go outside the bounds of the map
        self.pos.x = clamp(self.pos.x, 0, map_max_x - TILE_CAMERA_WIDTH)
        self.pos.y = clamp(self.pos.y, 0, map_max_y - self.tile_camera_height)

        
    def to_pixel_cord(self, pos):
        #dont draw anything outside of the screen
        if pos.x <= self.pos.x - 1 or pos.x >= self.pos.x + TILE_CAMERA_WIDTH or pos.y <= self.pos.y - 1 or pos.y >= self.pos.y + self.tile_camera_height:
            return None
        
        #relative cord to the camera's position
        relative_cord = pos.sub(self.pos) 
        #proportion cord from range [0, 1]
        proportion_cord = Vector(relative_cord.x / TILE_CAMERA_WIDTH, relative_cord.y / self.tile_camera_height)
        
        #multiply proportion cordinates by the screen dimensions for screen space coordinates
        screen_size = self.get_screen_dimensions()
        pixel_cord = Vector(proportion_cord.x * screen_size[0], proportion_cord.y * screen_size[1])
        return pixel_cord