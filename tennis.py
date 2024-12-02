import pygame, sys
pygame.init() 
clock = pygame.time.Clock()

green = (97, 190, 22)
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)   
pygame.display.set_caption('ap comp sci tennis')
screen.fill(green)

court = pygame.image.load("Images/tennis-court.png").convert_alpha()
court = pygame.transform.scale(court, (1475, 1475))
court = pygame.transform.smoothscale(court, screen.get_size())
screen.blit(court, (0, -250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)

