from pygame import *
from random import randint
font.init()
font1 = font.SysFont('Arial',45)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_hight):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (player_width, player_hight))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-100:
            self.rect.y += self.speed
    def update_r(self):
        keys =key.get_pressed()
        if  keys[K_u] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_j] and self.rect.y < win_height-100:
            self.rect.y += self.speed


ball = GameSprite('ball-removebg-preview.png', 200, 200, 4, 50, 50)
win_width = 700
win_height = 500
window = display.set_mode((700,500))
display.set_caption('ping_pong')
background = transform.scale(image.load('banana.jpg') , (700,500))
roc1 = Player('raketa2-removebg.png',5,30,5,30,150)
'''mixer.init()
mixer.music.load('Star Wars - John Williams - Duel Of the Fates.ogg')
mixer.music.play()'''
roc2 = Player('raketa2-removebg.png',670,5,5,30,150)
r1_lose = font1.render('игрок 1 aнскилл', True,(0,0,0))
r2_lose = font1.render('игрок 2 aнскилл', True,(0,0,0))

game = True
clock = time.Clock()
speed_y = 3
speed_x = 3
FPS  = 60
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(roc1, ball) or sprite.collide_rect(roc2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        
        roc1.update_l()
        roc2.update_r()
        roc1.reset()
        roc2.reset()
        ball.reset()
    if ball.rect.x > win_width:
        finish = True
        window.blit(r2_lose,(200,200))
    elif ball.rect.x <0:
        finish = True
        window.blit(r1_lose,(200,200))
    display.update()
    clock.tick(FPS)