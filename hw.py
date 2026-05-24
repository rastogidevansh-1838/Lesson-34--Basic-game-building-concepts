import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
window.fill((255, 255, 255))
pygame.display.set_caption('My first game screen')
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    done = pygame.font.Font(None, 42).render('HI I AM DEVANSH', True, pygame.Color('black'))
    pygame.draw.rect(window, (0, 135, 255), pygame.Rect(250, 150, 135, 140))
    pygame.display.flip()