from pygame import *


window = display.set_mode((700,500))




clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super(). __init__()
        self.image_name = player_image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
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
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

font.init()
font1 = font.Font(None,35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180,0,0))



racket1 = Player('racket.png', 5,10, 50, 100, 3)
racket2 = Player('racket.png', 640, 10, 50, 100, 3)   
ball = GameSprite('tenis_ball.png', 250, 250, 50, 50, 3)   

speed_x = 3
speed_y = 3

finish = False
run = True
while run:
       
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if finish != True:    
        window.fill((200,255,255))
        ball.reset()
        racket1.reset()
        racket2.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.top <= 0:
            speed_y *= -1
        if ball.rect.bottom >= 500:
            speed_y *= -1
        if ball.rect.colliderect(racket1.rect) or ball.rect.colliderect(racket2.rect):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x > 650:
            finish = True
            window.blit(lose2, (200,200))






    display.update()
    clock.tick(60)
