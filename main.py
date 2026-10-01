import sys
import pygame
import random

pygame.init()  # inicializa
pygame.font.init() #inicializa o "drivaer" de fonte
pygame.mixer.init() #inicializa o "drivaer" de fonte
pygame.display.set_caption("RPG do Omochain")
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()  #CLOCK
font = pygame.font.SysFont("Comic Sans MS", 30)
running = True
dt = 0

score = 0

music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

moedaPos = pygame.Vector2(200, 200)

colorPlayer = (0, 0, 255)

playerPos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:  # loop
    for event in pygame.event.get():
        pygame.display.flip()  # Update Screen
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")  # atualiza o fundo

    pnutText = f"Pontuação: {score}"

    p1 = pygame.draw.circle(screen, colorPlayer, playerPos, 20)

    mousePos = pygame.mouse.get_pos()  # detecta a posição do mouse
    mouse_rect = mousePos
    mouse = pygame.draw.circle(screen, "white", mouse_rect, 5)

    moeda = pygame.draw.circle(screen, "yellow", moedaPos, 10)

    pont = font.render(pnutText, False, (255, 255, 255))

    tecla = pygame.key.get_pressed()  # "driver" de teclado
    if tecla[pygame.K_w]:
        playerPos.y -= 300 * dt  # - = cima ou escquerda
    if tecla[pygame.K_s]:
        playerPos.y += 300 * dt  # + = baixo ou direita
    if tecla[pygame.K_a]:
        playerPos.x -= 300 * dt
    if tecla[pygame.K_d]:
        playerPos.x += 300 * dt

    if p1.colliderect(moeda):
        colorPlayer = (255, 0, 0)
        score += 1
        screen.blit(pont, (25, 25))
        moedaPos = pygame.Vector2(random.randrange(0, 600), random.randrange(0, 600))
    else:
        colorPlayer = (0, 0, 255)

    screen.blit(pont, (25, 25))

    dt = clock.tick(60) / 1000  # FPS

    pygame.display.update()

pygame.quit()