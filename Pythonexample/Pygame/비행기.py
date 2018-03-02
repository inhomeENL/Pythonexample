import pygame
import sys
import random
import time
from pygame.locals import *

#초당 프레임 수
FPS = 30
#윈도우 크기
WINDOWWIDTH = 960
WINDOWHEIGHT = int(WINDOWWIDTH / 2)

#배경 최대 크기
ORIGINBACKGROUNDWIDTH = 1280
ORIGINBACKGROUNDHEIGHT = 640

#스프라이트 속도
BACKGROUNDSPEED = 2
FIREBALLSPEED = 15
#색
WHITE = (255, 255, 255)

#윈도우 설정하기
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("PyFlying")

class Boom(pygame.sprite.Sprite):
    """
    박쥐가 골로 갔을때 폭발 이미지
    """
    BOOMTIME = 5

    def __init__(self, x, y):
        global IMAGESDICT
        super().__init__()
        self.image = IMAGESDICT["boom"]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.time = 0

    def update(self):
        self.time += 1
        if self.time >= self.BOOMTIME:
            self.kill()

class BatEnemy(pygame.sprite.Sprite):
    """..."""
    BATSPEED = 7
    BATTIME = 3
    bat_num = 0
    bat_remove_time = 0

    def __init__(self):
        """..."""
        global IMAGESDICT
        super().__init__()
        self.image = IMAGESDICT["bat"]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = init_enemy_pos(IMAGESDICT["bat"])
        BatEnemy.bat_num += 1

    def __del__(self):
        """..."""
        BatEnemy.bat_num -= 1
        BatEnemy.bat_remove_time = time.time()

    def update(self):
        self.rect = self.rect.move(-self.BATSPEED, 0)
        if self.rect.left < 0:
            self.kill()

    def position(self):
        return self.rect.left, self.rect.top

class AirplaneBullet(pygame.sprite.Sprite):
    """..."""
    BULLETSPEED = 0

    def __init__(self, airplaneX, airplaneY):
        """..."""
        global IMAGESDICT
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGESDICT["bullet"]
        self.rect = self.image.get_rect()
        self.rect.left = airplaneX + IMAGESDICT["airplane"].get_width()
        self.rect.top = airplaneY + IMAGESDICT["airplane"].get_height()/2
        self.born_time = time.time()
        print("bullet born")
        print("time: %s" %self.born_time)

    def BulletSpeed(self):
        if time.time() < self.born_time + 0.5:
            print("대기")
            return 0
        else:
            print("set")
            return (time.time() - self.born_time)*8

    def update(self):
        """..."""
        self.rect = self.rect.move(self.BulletSpeed(), 0)
        if self.rect.left > WINDOWWIDTH:
            self.kill()

def init_enemy_pos(image):
    """..."""
    x = WINDOWWIDTH
    y = random.randrange(0, WINDOWHEIGHT - image.get_height())
    return x, y

def draw_object(image, x, y):
    """..."""
    global DISPLAYSURF
    DISPLAYSURF.blit(image, (x,y))

def main():
    global FPSCLOCK, DISPLAYSURF
    global IMAGESDICT

    #비행기 왼쪽 초기 위치
    airplaneX = WINDOWWIDTH * 0.05
    airplaneY = WINDOWHEIGHT * 0.8
    airplaneY_change = 0
    airplaneX_change = 0
    
    #비행기 크기
    AIRPLANEWIDTH = IMAGESDICT["airplane"].get_width()
    AIRPLANEHEIGHT = IMAGESDICT["airplane"].get_height()

    #윈도우 변경에 따른 배경크기 변경
    BACKGROUNDWIDTH = IMAGESDICT["background"].get_width()

    #배경 초기 위치
    background_x = 0
    other_background_x = BACKGROUNDWIDTH

    #파이어볼 초기화 및 초기 위치
    #2/7확률로 파피어볼이 날아감
    fireball_choice = random.randint(1,7)
    if fireball_choice == 1 or fireball_choice == 2:
        fireball_x, fireball_y = init_enemy_pos(IMAGESDICT["fireball%s" % fireball_choice])
    else:
        fireball_x, fireball_y = WINDOWWIDTH, 0

    #총알 sprite group
    bullet_group = pygame.sprite.Group()
    bat_group = pygame.sprite.Group()
    boom_group = pygame.sprite.Group()

    #전체 sprite group
    sprite_group = pygame.sprite.Group()

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                        airplaneY_change = -5
                elif event.key == K_DOWN:
                        airplaneY_change = 5
                elif event.key == K_RIGHT:
                    airplaneX_change = 5
                elif event.key == K_LEFT:
                    airplaneX_change = -5
                if event.key == K_LCTRL:
                    #총알을 추가한다.
                    bullet_group.add(AirplaneBullet(airplaneX, airplaneY))
                    sprite_group.add(bullet_group)
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    airplaneY_change = 0
                elif event.key == K_RIGHT or event.key == K_LEFT:
                    airplaneX_change = 0
                    
        #비행기 위치 제한
        airplaneY += airplaneY_change
        if airplaneY < 0:
            airplaneY = 0
        elif airplaneY > WINDOWHEIGHT - AIRPLANEHEIGHT:
            airplaneY = WINDOWHEIGHT - AIRPLANEHEIGHT

        airplaneX += airplaneX_change
        if airplaneX < 0:
            airplaneX = 0
        elif airplaneX > WINDOWWIDTH - AIRPLANEWIDTH:
            airplaneX = WINDOWWIDTH - AIRPLANEWIDTH

        #배경 그리기
        background_x -= BACKGROUNDSPEED
        if background_x == -BACKGROUNDWIDTH:
            background_x = BACKGROUNDWIDTH
        draw_object(IMAGESDICT["background"], background_x, 0)

        other_background_x -= BACKGROUNDSPEED
        if other_background_x == -BACKGROUNDWIDTH:
            other_background_x = BACKGROUNDWIDTH
        draw_object(IMAGESDICT["background"], other_background_x, 0)

        #박쥐 위치 설정
        if BatEnemy.BATTIME <= time.time() - BatEnemy.bat_remove_time \
            and BatEnemy.bat_num <= 0:
            bat_group.add(BatEnemy())
            sprite_group.add(bat_group)

        #파이어볼 위치설정
        if fireball_choice == 1 or fireball_choice == 2:
            fireball_x -= FIREBALLSPEED
        else:
            fireball_x -= 2*FIREBALLSPEED

        if fireball_x <=0:
            fireball_choice = random.randint(1,7)
            if fireball_choice == 1 or fireball_choice == 2:
                fireball_x, fireball_y = init_enemy_pos(IMAGESDICT["fireball%s"%fireball_choice])
            else:
                fireball_x, fireball_y = WINDOWWIDTH, 0

        #bullet이 지정된 group에 있는 모든 sprite의 update함수를 실행한다.
        sprite_group.update()
        bullet_group.update()

        #충돌 검사
        bat_collision_dict = pygame.sprite.groupcollide(bullet_group, bat_group, False, False)
        if bat_collision_dict:
            for bullet in bat_collision_dict.keys():
                bat_x, bat_y = bat_collision_dict[bullet][0].position()
                boom_group.add(Boom(bat_x, bat_y))
            sprite_group.add(boom_group)
            pygame.sprite.groupcollide(bullet_group, bat_group, True, True)

        #다른 스프라이트 그리기
        draw_object(IMAGESDICT["airplane"], airplaneX, airplaneY)
        if fireball_choice == 1 or fireball_choice == 2:
            draw_object(IMAGESDICT["fireball%s" %fireball_choice], fireball_x, fireball_y)
        sprite_group.draw(DISPLAYSURF)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def game_init():
    global FPSCLOCK, DISPLAYSURF
    global IMAGESDICT
    FPSCLOCK = pygame.time.Clock()
    pygame.init()

    #DISPLAY Surface 설정하기
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyFlying')

    #이미지 받아오기
    IMAGESDICT = {"airplane": pygame.image.load("plane.png"),
                  "background": pygame.image.load("background.png"),
                  "bat":pygame.image.load("cat.png"),
                  "fireball1":pygame.image.load("fireball1.png"),
                  "fireball2":pygame.image.load("fireball2.png"),
                  "bullet":pygame.image.load("bullet.png"),
                  "boom": pygame.image.load('boom.png')}

    #배경 이미지 게임 윈도우 크기에 맞추기
    assert WINDOWWIDTH <= ORIGINBACKGROUNDWIDTH or WINDOWHEIGHT <= ORIGINBACKGROUNDHEIGHT,"게임 윈도우 크기가 너무 큽니다."
    IMAGESDICT["background"] = pygame.transform.scale(IMAGESDICT["background"], (WINDOWWIDTH, WINDOWHEIGHT))

    main()

if __name__ == '__main__':
    game_init()
