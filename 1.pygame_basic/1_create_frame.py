import pygame

pygame.init() #initialize -> 필수

#frame size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#title setting
pygame.display.set_caption("Nado Game")

#event loop
running = True # game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()