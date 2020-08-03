import pygame

pygame.init() #initialize -> 필수

#frame size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#title setting
pygame.display.set_caption("Nado Game")
background = pygame.image.load("C:/Users/User/Desktop/Python/pygame_basic/background.png")

# load sprite(character)
character = pygame.image.load("C:/Users/User/Desktop/Python/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = screen_width/2 - character_width/2
character_ypos = screen_height - character_height

#event loop
running = True # game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    screen.blit(character, (character_xpos, character_ypos))

    pygame.display.update()

pygame.quit()