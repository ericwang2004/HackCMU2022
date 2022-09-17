from random import random
import sys
from pygame import draw as pydraw
from pygame import Rect
import pygame
import random
from vector import Vector
import pygame
import os

EMPTY = 0 
WALL = 1
MAGIC = 2

#WHITE BLACK RED
COLORS = [(255, 255, 255), (0, 0, 0), (0, 0, 255)]
MAGIC_CONNECT_COLOR = (100, 10, 200)

class Editor:
    def __init__(self, rows, cols, width_pixels, height_pixels) -> None:
        self.map = [[random.randint(0, 2) for i in range(cols)] for j in range(rows)]
        self.rows = rows
        self.cols = cols
        self.width_pixels = width_pixels
        self.heigh_pixels = height_pixels
        self.step_x = width_pixels / self.cols
        self.step_y = height_pixels / self.rows
        
        self.magic_connect_tile = None
        self.connect_magic = False
        
        self.magic_connections = dict()
        
    def input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cords = pygame.mouse.get_pos()
            clamped = (int(mouse_cords[0] // self.step_x), int(mouse_cords[1] // self.step_y))
            
            if event.button == 1: #left click
                if clamped[0] >= 0 and clamped[0] < self.cols and clamped[1] >= 0 and clamped[1] < self.rows:
                    if self.map[clamped[1]][clamped[0]] == MAGIC and self.magic_connections.__contains__(clamped):
                        self.magic_connections.pop(clamped)
                        
                    self.map[clamped[1]][clamped[0]] = (self.map[clamped[1]][clamped[0]] + 1) % 3
                    
            elif event.button == 3:
                if self.map[clamped[1]][clamped[0]] != MAGIC:
                    return
                
                if self.connect_magic: #if the arrow is already being drawn, complete the connection
                    print("HAHHAHAHAHAH IM HERE!!!!!!!1", clamped)
                    self.magic_connections[self.magic_connect_tile] = clamped
                    print(self.magic_connections.__len__())
                    self.connect_magic = False
                    self.magic_connect_tile = None
                else:
                    
                    #if the tile has not been connected to something....
                    if not self.magic_connections.__contains__(clamped):
                         self.connect_magic = True
                         self.magic_connect_tile = clamped
                    else: #if it has, then remove the previous connection from the hashmap
                         print("HAHHAHAHAHAH IM WHWAHAHAHHAHHWHW KEKEKEKEKEKKEKEE HERE!!!!!!!1", clamped)
                         self.magic_connections.pop(clamped)
                         self.connect_magic = True
                         self.magic_connect_tile = clamped
                
    
    def draw_arrow(self, display, p1, p2):
        #print("HEHEHEHEHHE", p1)
        p1 = Vector(p1[0], p1[1], 0)
        p2 = Vector(p2[0], p2[1], 0)
        disp_vector = p2.sub_new(p1)
        disp_vector.normalize()
        perp_vector = Vector(0, 0, 1).cross(disp_vector)
        
        half_extents = perp_vector.mult_new(0.5)
        
        bleft = p1.add_new(half_extents.mult_new(-1))
        bright = p1.add_new(half_extents)
        
        tleft = p2.add_new(half_extents.mult_new(-1))
        tright = p2.add_new(half_extents)

        LINE_COLOR = (255, 255, 255)
        print(((type(bleft.x), bleft.y),(bright.x, bright.y),(tleft.x, tleft.y),(tright.x, tright.y)))
        pygame.draw.polygon(display, LINE_COLOR, ((bleft.x.real, bleft.y.real),(bright.x.real, bright.y.real),(tleft.x.real, tleft.y.real),(tright.x.real, tright.y.real)))
    
    def draw_arrow_2(self, display, p1, p2):
        LINE_COLOR = (255, 255, 255)
        p1 = (p1[0] * self.step_x, p1[1] * self.step_y)
        pygame.draw.line(display, LINE_COLOR, p1, p2, width=int(self.step_x / 2))
        
    def render(self, display):
        
        for y in range(self.rows):
            for x in range(self.cols):
                color = COLORS[self.map[y][x]]
                
                if self.magic_connections.__contains__((x, y)) or (x, y) in self.magic_connections.values():
                     color = MAGIC_CONNECT_COLOR
                pydraw.rect(display, color, Rect(self.step_x * x, self.step_y * y, self.step_x, self.step_y))
                
        if self.connect_magic:
          self.draw_arrow_2(display, self.magic_connect_tile, pygame.mouse.get_pos())
                
    def save(self, path):
        NAMES = ['EMPTY', 'WALL', 'MAGIC']
        print(self.magic_connections)
        with open(path, "w") as f:
            f.write(f'Dimensions:{(self.rows, self.cols)}')
            for y in range(self.rows):
                for x in range(self.cols):
                    typ = self.map[y][x]
                    f.write(f"({x}, {y}): {NAMES[typ]}")
                    
                    if typ == MAGIC:
                        if not self.magic_connections.__contains__((x, y)) and not (x, y) in self.magic_connections.values():
                            print("ERROR: Must have each magic tile connected to another!")
                            sys.exit()
                        
                        tile = None
                        if self.magic_connections.__contains__((x, y)):
                            tile = self.magic_connections[(x, y)] 
                
                        if not tile:
                            for (a, b) in self.magic_connections.items():
                                if b == (x, y):
                                    tile = a
                                    break
                                
                        f.write(f": {tile}")
                    f.write("\n")