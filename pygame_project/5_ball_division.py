import os
import pygame
#########################################################
# 기본 초기화
pygame.init() #initialize -> 필수

#frame size setting
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#title setting
pygame.display.set_caption("Nado Pang")

#fps
clock = pygame.time.Clock()
#########################################################

# 1. 사용자 게임 초기화: 배경화면, 게임 이미지, 좌표, 속도, 폰트 등
current_path = os.path.dirname(__file__) #현재 파일위치
image_path = os.path.join(current_path, "images")

#background
background = pygame.image.load(os.path.join(image_path, "background.png"))

#stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = screen_width/2 - character_width/2
character_ypos = screen_height - stage_height - character_height

character_to_x = 0
character_speed = 5

#weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []
weapon_speed = 10

#ball
ball_images = [
    pygame.image.load(os.path.join(image_path, "ball1.png")),
    pygame.image.load(os.path.join(image_path, "ball2.png")),
    pygame.image.load(os.path.join(image_path, "ball3.png")),
    pygame.image.load(os.path.join(image_path, "ball4.png"))
]
ball_speed_y = [-18, -15, -12, -9]

balls = []
balls.append({
    "pos_x": 50,
    "pos_y": 50,
    "img_idx": 0,
    "to_x": 3,
    "to_y": -6,
    "init_spd_y": ball_speed_y[0]
})

weapon_to_remove = -1
ball_to_remove = -1

running = True 
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_xpos = character_xpos + character_width/2 - weapon_width/2
                weapon_ypos = character_ypos
                weapons.append([weapon_xpos, weapon_ypos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x=0
       
    # 3. 게임 캐릭터 위치 정의
    character_xpos += character_to_x
    if character_xpos < 0 : 
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width
    
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0] #0 이상인 경우만 남기기

    for ball_idx, ball_val in enumerate(balls):
        ball_xpos = ball_val["pos_x"]
        ball_ypos = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_xpos < 0 or ball_xpos > screen_width - ball_width:
            ball_val["to_x"] = -ball_val["to_x"]
        if ball_ypos >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos

    for ball_idx, ball_val in enumerate(balls):
        ball_xpos = ball_val["pos_x"]
        ball_ypos = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_xpos
        ball_rect.top = ball_ypos

        if character_rect.colliderect(ball_rect):
            running=False
            break 

        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_xpos = weapon_val[0]
            weapon_ypos = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_xpos
            weapon_rect.top = weapon_ypos

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

                # ball is not the smallest
                if ball_img_idx < 3:
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    small_ball_rect = ball_images[ball_img_idx+1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    balls.append({
                        "pos_x": ball_xpos + ball_width/2 - small_ball_width/2,
                        "pos_y": ball_ypos + ball_height/2 - small_ball_height/2,
                        "img_idx": ball_img_idx + 1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1] })
                    balls.append({
                        "pos_x": ball_xpos + ball_width/2 + small_ball_width/2,
                        "pos_y": ball_ypos + ball_height/2 - small_ball_height/2,
                        "img_idx": ball_img_idx + 1,
                        "to_x": 3,
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1] })

                break
    
    #remove ball or weapon
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    for weapon_xpos, weapon_ypos in weapons:
        screen.blit(weapon, (weapon_xpos, weapon_ypos))
    for idx, val in enumerate(balls):
        ball_xpos = val["pos_x"]
        ball_ypos = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_xpos, ball_ypos))
    screen.blit(character, (character_xpos, character_ypos))

    pygame.display.update()


pygame.quit()