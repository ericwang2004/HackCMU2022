import sys
from turtle import screensize
from state import State
import pygame

BACKGROUND_COLOR = (100, 200, 150)

white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)

class gameOver(State):
    def __init__(self, camera) -> None:
        super().__init__()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render("GAME OVER LOSER", False, orange, yellow)
        screen_size = camera.get_screen_dimensions()
        self.JUNGKOOK = pygame.transform.scale(pygame.image.load("./asset/Leonard.jpeg"), (screen_size[0] * 1.8, screen_size[1]))
    
    def render(self, display, camera):
        screen_size = camera.get_screen_dimensions()
        display.fill(BACKGROUND_COLOR)
        display.blit(self.JUNGKOOK, (0, 0))
        display.blit(self.text, (screen_size[0] / 2, screen_size[1] / 2))
        return super().render(display, (screen_size[0] / 2 - screen_size[0] / 6, screen_size[1] / 2))
    
    def input(self, event, camera):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("GOOTBYE")
            sys.exit()
    
    def update(self, delta, camera):
        return False