import pygame


class Snake:
    def __init__(self):
        self.perso = [pygame.math.Vector2(5,10), pygame.math.Vector2(4,10), pygame.math.Vector2(3,10)]
        self.direction = pygame.math.Vector2(1,0)
        self.grow = False 

    def drawsnake(self, case, ecran):
        for bloc in self.perso:
            posx = int(bloc.x * case)
            posy = int(bloc.y * case)
            snakerect = pygame.Rect(posx, posy, case, case)
            pygame.draw.rect(ecran,(183, 191, 122), snakerect)
    
    def move(self):
        if self.grow == True:
            persomove = self.perso[:]
            persomove.insert(0, persomove[0] + self.direction)
            self.perso = persomove[:]
            self.grow = False
        else:
            persomove = self.perso[:-1]
            persomove.insert(0, persomove[0] + self.direction)
            self.perso = persomove[:]

    def growth(self):
        self.grow = True

    def resetgame(self):
        self.perso = [pygame.math.Vector2(5,10), pygame.math.Vector2(4,10), pygame.math.Vector2(3,10)]
        self.direction = pygame.math.Vector2(0,0)