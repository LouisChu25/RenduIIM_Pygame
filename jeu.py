import pygame, sys
from fruit import Fruit
from snake import Snake
from bomb import Bomb

taille_cases = 20
nb_cases = 35
ecran = pygame.display.set_mode((taille_cases * nb_cases, taille_cases * nb_cases))

class Jeu:
    def __init__(self, nbcases):
        self.fruit = Fruit(nbcases)
        self.bomb = Bomb(nbcases)
        self.snake = Snake()
        self.fontjeu = pygame.font.Font(None, 30)
    
    def interactions(self, nbcases):
        self.snake.move()
        self.eat(nbcases)
        self.collision(nbcases)

    def create_elements(self, case, ecran, imgpomme, imgbombe, nbcases, font, seconds):
        self.fruit.drawfruit(case, imgpomme)
        self.bomb.drawbomb(case, imgbombe)
        self.snake.drawsnake(case, ecran)
        self.scoring(nbcases, ecran, case, font)
        self.bomb.countdown(ecran, case, font, seconds)
        self.start_text(ecran, font)
    
    def eat(self, nbcases):
        if self.fruit.pos == self.snake.perso[0]:
            self.fruit.newfruit(nbcases)
            self.snake.growth()

    def collision(self, nbcases):
        if self.snake.perso[0].x < 0 or self.snake.perso[0].x > nbcases:
            self.gameover()
        if self.snake.perso[0].y < 0 or self.snake.perso[0].y > nbcases:
            self.gameover()
        for bloc in self.snake.perso[1:]:
            if bloc == self.snake.perso[0]:
                self.gameover()

    def gameover(self):
        self.snake.resetgame()

    def scoring(self, nbcases, screen, case, fontjeu):
        score = str(len(self.snake.perso) - 3)
        scoresurface = fontjeu.render(score, True, (56,74,12))
        scorepos = (int(case * nbcases -20), int(case +20))
        scorerect = scoresurface.get_rect(center = scorepos)
        screen.blit(scoresurface, scorerect)

    def start_text(self, ecran, font):
        start_surface = font.render("Press SPACE to start or reset", True, (56,74,12))
        start_pos = (int(35 * 20 / 2), 40)
        start_rect = start_surface.get_rect(center = start_pos)
        ecran.blit(start_surface, start_rect)