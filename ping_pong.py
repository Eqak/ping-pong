from pygame import *
import time as tm
window = display.set_mode((700, 500))
display.set_caption('Пинг понг')

background = transform.scale(image.load('fon.jpg'), (700, 500))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_weight, player_height, player_speed, x_speed = None, y_speed = None):
        super().__init__()
        self.weight = player_weight
        self.height = player_height
        self.image = transform.scale(image.load(player_image), (self.weight, self.height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x_speed = x_speed
        self.y_speed = y_speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, enemy):
        if sprite.collide_rect(self, enemy):
            return True
        else:
            return False



class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
    
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.y <= 0:
            self.x_speed *= 1
            self.y_speed *= -1

        if self.rect.y >= 445:
            self.x_speed *= 1
            self.y_speed *= -1
    

font.init()
font2 = font.SysFont('Arial', 45)
font1 = font.SysFont('Arial', 30)

lose1 = font2.render('Первый игрок проиграл!', True, (255, 0, 0))
lose2 = font2.render('Второй игрок проиграл!', True, (255, 0, 0))


racket1 = Player('wall.jpg', 50, 250, 20, 65, 5)
racket2 = Player('wall.jpg', 650, 250, 20, 65, 5)
ball = Ball('мяч.png', 350, 250, 50, 50, 0, 5, 3)

health_1 = 3
health_2 = 3

game = True
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0, 0))

        text_health1 = font1.render('Жизни:' + str(health_1), 1, (255, 255, 255))
        text_health2 = font1.render('Жизни:' + str(health_2), 1, (255, 255, 255))

        window.blit(text_health1, (10, 10))
        window.blit(text_health2, (600, 10))

        racket1.update_l()
        racket2.update_r()
        ball.update()


        racket1.reset()
        racket2.reset()
        ball.reset()
        
            
        if ball.colliderect(racket1):
            ball.x_speed *= -1
            ball.y_speed *= 1
        
        if ball.colliderect(racket2):
            ball.x_speed *= -1
            ball.y_speed *= 1

    
        if ball.rect.x >= 700:
            health_2 -= 1
            ball.rect.x = 350
            ball.rect.y = 250
        
        if ball.rect.x <= 0:
            health_1 -= 1
            ball.rect.x = 350
            ball.rect.y = 250
            
        if health_1 <= 0:
            finish = True
            window.blit(lose1, (150, 225))
            
        if health_2 <= 0:
            finish = True
            window.blit(lose2, (150, 225))

        display.update()
        clock.tick(FPS)