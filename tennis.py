import pygame, sys
pygame.init() 
clock = pygame.time.Clock()

#colors
bgcolor = (232, 0, 255)
playersidecolor = (97, 190, 22)
cpusidecolor = (50, 171, 199)
oobcolor = (173, 40, 40)

#bg screen
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)   
pygame.display.set_caption('ap comp sci tennis')
screen.fill(bgcolor)

#objects

court = pygame.image.load("Images/tennis-court.png").convert_alpha()
court = pygame.transform.smoothscale(court,(0.9*screen_width,1.5*screen_height))
playerside = pygame.draw.rect(screen, playersidecolor, pygame.Rect(0, 0, screen_width/2, screen_height))
cpuside = pygame.draw.rect(screen, cpusidecolor, pygame.Rect(screen_width/2, 0, screen_width/2, screen_height))
oobleft = pygame.draw.rect(screen, oobcolor, pygame.Rect(0, 0, screen_width/20, screen_height))
oobright = pygame.draw.rect(screen, oobcolor, pygame.Rect(0.95*screen_width, 0, screen_width/20, screen_height))
oobtop = pygame.draw.rect(screen, oobcolor, pygame.Rect(0, 0, screen_width, screen_height/7.2))
oobbottom = pygame.draw.rect(screen, oobcolor, pygame.Rect(0, 0.85*screen_height, screen_width, screen_height/7.2))
screen.blit(court, (screen_width/20, -screen_height/4))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)

