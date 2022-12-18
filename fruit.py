import pygame, random

taille_cases = 20
nb_cases = 35
ecran = pygame.display.set_mode((taille_cases * nb_cases, taille_cases * nb_cases))

class Fruit:
    def __init__(self, nbrcases):
        self.newfruit(nbrcases)

    def drawfruit(self, case, imgpomme):
        fruitrect = pygame.Rect(int(self.pos.x * case), int(self.pos.y * case), case, case)
        ecran.blit(imgpomme, fruitrect)
        # pygame.draw.rect(ecran, (126, 166, 114), fruitrect)

    def newfruit(self, nbcases):
        self.x = random.randint(0, nbcases-1)
        self.y = random.randint(0, nbcases-1)
        self.pos = pygame.math.Vector2(self.x,self.y)