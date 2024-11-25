import pygame, sys
pygame.init() 
clock = pygame.time.Clock()

screen_width = 3840
screen_height = 2160
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ap comp sci tennis')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)

