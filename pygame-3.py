import pygame, sys
from jeu import Jeu

pygame.init()
taille_cases = 20
nb_cases = 35
ecran = pygame.display.set_mode((taille_cases * nb_cases, taille_cases * nb_cases))
fps = pygame.time.Clock()
pomme = pygame.image.load('img/pomme.png').convert_alpha()
pomme = pygame.transform.scale(pomme, (20,20))
bombe = pygame.image.load('img/bomb.png').convert_alpha()
bombe = pygame.transform.scale(bombe, (20,20))
mecaniques = Jeu(nb_cases)

font = pygame.font.SysFont('Helvetica', 20)

tempo = pygame.USEREVENT
pygame.time.set_timer(tempo, 100)
start_ticks=pygame.time.get_ticks() 
game_start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == tempo:
            mecaniques.interactions(nb_cases)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if mecaniques.snake.direction.y != 1:
                    mecaniques.snake.direction = pygame.math.Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if mecaniques.snake.direction.y != -1:
                    mecaniques.snake.direction = pygame.math.Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if mecaniques.snake.direction.x != 1:
                    mecaniques.snake.direction = pygame.math.Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if mecaniques.snake.direction.x != -1:
                    mecaniques.snake.direction = pygame.math.Vector2(1, 0)
            if event.key == pygame.K_SPACE:
                start_ticks = pygame.time.get_ticks()
                mecaniques.gameover()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mecaniques.bomb.checkClick(nb_cases) == True:
                    start_ticks = pygame.time.get_ticks()

    seconds = 6 - ((pygame.time.get_ticks() - start_ticks) / 1000) 
    if seconds <= 0:
        start_ticks = pygame.time.get_ticks()
        mecaniques.gameover()
        
    ecran.fill((175,215,70))
    mecaniques.create_elements(taille_cases, ecran, pomme, bombe, nb_cases, font, seconds)

    pygame.display.update()
    fps.tick(60)
    while not game_start:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_ticks = pygame.time.get_ticks()
                game_start = True
                pygame.event.clear()
                break