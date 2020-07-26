import pygame
#########################################################
# 기본 초기화
pygame.init() #initialize -> 필수

#frame size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#title setting
pygame.display.set_caption("Nado Game")

#fps
clock = pygame.time.Clock()
#########################################################

# 1. 사용자 게임 초기화: 배경화면, 게임 이미지, 좌표, 속도, 폰트 등

running = True 
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리
    
    # 5. 화면에 그리기

    pygame.display.update()


pygame.quit()