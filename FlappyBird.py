import pygame
import random
import time
random.seed(time.ctime())

pygame.init()

font = pygame.font.Font(None, 36)

ScreenWidth = 1600
ScreenHeight = 1000

screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

player = pygame.Rect((300, 250, 50, 50))

playerYPos = 250

#makes three random pipes that work for 3 diffrent presets
pipeFormation = random.randint(1, 3)
if pipeFormation == 1:
    pipeXPos = 1600
    initXPos = 1600
    topPipe = pygame.Rect((initXPos, -350, 100, 1000))
    bottomPipe = pygame.Rect((initXPos, 950, 100, 1000))
elif pipeFormation == 2:
    pipeXPos = 1600
    initXPos = 1600
    topPipe = pygame.Rect((initXPos, -650, 100, 1000))
    bottomPipe = pygame.Rect((initXPos, 650, 100, 1000))
elif pipeFormation == 3:
    pipeXPos = 1600
    initXPos = 1600
    topPipe = pygame.Rect((initXPos, -950, 100, 1000))
    bottomPipe = pygame.Rect((initXPos, 350, 100, 1000))

run = True

jumpAvaliable = True

score = 0

def reset():
    score = 0
    newPipe()

def newPipe():
    pipeFormation = random.randint(1, 3)
    if pipeFormation == 1:
        topPipe.update(initXPos, -350, 100, 1000)
        bottomPipe.update(initXPos, 950, 100, 1000)
    if pipeFormation == 2:
        topPipe.update(initXPos, -650, 100, 1000)
        bottomPipe.update(initXPos, 650, 100, 1000)
    if pipeFormation == 3:
        topPipe.update(initXPos, -950, 100, 1000)
        bottomPipe.update(initXPos, 350, 100, 1000)
    pipeXPos = 1600
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 0, 255), topPipe)
    pygame.draw.rect(screen, (0, 255, 0), bottomPipe)

    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    #player movement 
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and jumpAvaliable:
        player.move_ip(0, -8)
        playerYPos -= 8
        jumpAvaliable = False
    else:
        jumpAvaliable = True

    #gravity        
    player.move_ip(0, 2)
    playerYPos += 2
    #pipe movement
    topPipe.move_ip(-2, 0)
    bottomPipe.move_ip(-2, 0)
    pipeXPos -= 2

    if playerYPos < 0:
        pygame.quit()
    if playerYPos > ScreenHeight:
        pygame.quit()

    if pipeXPos < 0:
        score += 1
        pipeFormation = random.randint(1, 3)
        if pipeFormation == 1:
            topPipe.update(initXPos, -350, 100, 1000)
            bottomPipe.update(initXPos, 950, 100, 1000)
        if pipeFormation == 2:
            topPipe.update(initXPos, -650, 100, 1000)
            bottomPipe.update(initXPos, 650, 100, 1000)
        if pipeFormation == 3:
            topPipe.update(initXPos, -950, 100, 1000)
            bottomPipe.update(initXPos, 350, 100, 1000)
        pipeXPos = 1600
    if player.colliderect(topPipe) or player.colliderect(bottomPipe):
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()