import pygame, random


taille_cases = 20
nb_cases = 35
ecran = pygame.display.set_mode((taille_cases * nb_cases, taille_cases * nb_cases))

class Bomb:
    def __init__(self, nbrcases):
        self.newbomb(nbrcases)

    def drawbomb(self, case, imgpomme):
        fruitrect = pygame.Rect(int(self.pos.x * case), int(self.pos.y * case), case, case)
        ecran.blit(imgpomme, fruitrect)
        # pygame.draw.rect(ecran, (126, 166, 114), fruitrect)

    def newbomb(self, nbcases):
        self.x = random.randint(0, nbcases-1)
        self.y = random.randint(0, nbcases-1)
        self.pos = pygame.math.Vector2(self.x,self.y)

    def checkClick(self, nbcases):
        pos = pygame.mouse.get_pos()
        x = pos[0] / taille_cases
        y = pos[1] / taille_cases
        newpos = (x, y)
        if newpos[0] >= self.pos.x and newpos[0] <= (self.pos.x + 1) and newpos[1] >= self.pos.y and newpos[1] <= (self.pos.y + 1):
            self.newbomb(nbcases)
            return True
        return False
    
    def countdown(self, screen, case, fontjeu, seconds):
        scoresurface = fontjeu.render(f"Bomb: {str(int(seconds))}", True, (56,74,12))
        scorepos = (int(case+20), int(case +20))
        scorerect = scoresurface.get_rect(center = scorepos)
        screen.blit(scoresurface, scorerect)