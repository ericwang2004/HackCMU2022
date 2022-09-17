
import sys
import pygame


class Animator:
    def __init__(self, sprite_sheet, num_animations, num_frames, delay) -> None:
        self.sprite_sheet = sprite_sheet
        self.num_anis = num_animations
        self.num_frames = num_frames
        self.delay = delay
        self.cumulative_time = 0.0
        self.current_animation = 0
        self.current_frame = 0
        
    def update(self, delta_time):
        self.cumulative_time += delta_time
        if self.cumulative_time >= self.delay:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.cumulative_time -= self.delay
    
    def swap_animation(self, animation_index):
        if animation_index < 0 or animation_index >= self.num_anis:
            print(f"invalid animation index! Must be between 0 and {self.num_anis}")
            sys.exit()
        self.current_animation = animation_index
    
    def get_frame(self, display):
        step_x = self.sprite_sheet.get_width() / self.num_frames
        step_y = self.sprite_sheet.get_height() / self.num_anis
        
        rect = pygame.Rect((step_x * self.current_frame, step_y * self.current_animation, 
                            step_x * self.current_frame + step_x, step_y * self.current_animation + step_y))
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image