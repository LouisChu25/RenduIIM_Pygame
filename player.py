import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
    def move_right(self):
        self.x += 1
    def move_left(self):
        self.x -= 1