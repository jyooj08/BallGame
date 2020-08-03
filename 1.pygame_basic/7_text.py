import pygame

pygame.init() #initialize -> 필수

#frame size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#title setting
pygame.display.set_caption("Nado Game")

#fps
clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/User/Desktop/Python/pygame_basic/background.png")

# load sprite(character)
character = pygame.image.load("C:/Users/User/Desktop/Python/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = screen_width/2 - character_width/2
character_ypos = screen_height - character_height

to_x = 0
to_y = 0
character_speed = 0.6

#enemy
# load sprite(character)
enemy = pygame.image.load("C:/Users/User/Desktop/Python/pygame_basic/enemy.png")
enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_xpos = screen_width/2 - enemy_width/2
enemy_ypos = screen_height/2 - enemy_height/2

#text
game_font = pygame.font.Font(None, 40) # font object

total_time = 10
start_ticks = pygame.time.get_ticks()

#event loop
running = True # game is running
while running:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # any key is pressed
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0
    
    character_xpos += to_x * dt
    character_ypos += to_y * dt

    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width
    if character_ypos < 0:
        character_ypos = 0
    elif character_ypos > screen_height - character_height:
        character_ypos = screen_height - character_height

    #collision
    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xpos
    enemy_rect.top = enemy_ypos

    if character_rect.colliderect(enemy_rect):
        print("collision occur")
        running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_xpos, character_ypos))
    screen.blit(enemy, (enemy_xpos, enemy_ypos))

    #time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #second
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))
    if total_time - elapsed_time <= 0:
        print("timeout")
        running = False

    pygame.display.update()

pygame.time.delay(2000) # delay 2 seconds

pygame.quit()