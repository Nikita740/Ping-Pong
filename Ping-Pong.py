from pygame import *
from random import randint
from time import time as timer #импортируем функцию для засекания времени, чтобы интерпретатор не искал эту функцию в pygame модуле time, даём ей другое название сами
#подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.SysFont("Arial", 80)
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (wight, height))
       self.speed = player_speed
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
#метод, отрисовывающий героя на окне
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 5:
            self.rect.y += self.speed
  
#создаём окошко
win_width = 600
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
bricks = "bricks.jpg"
background = transform.scale(image.load(bricks), (win_width, win_height))
line = "line.png"
ball_img = "ball.jpg"
player1 = Player(line, 1,200,4,150,150)
player2 = Player(line, 510,200,4,150,150)
ball = GameSprite(ball_img,200,200,0.3,50,50)
finish = False
FPS = 60
clock = time.Clock()
font = font.Font(None, 35)
lose1 = font.render("Player 1 LOSE!", True, (180,0,0))
lose2 = font.render("Player 2 LOSE!", True, (180,0,0))
speed_x = 1.5
speed_y = 1.5
game = True #флаг сбрасывается кнопкой закрытия окна

while game:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background,(0,0))
        player1.update_l()
        player2.update_r()
        ball.rect.x += speed_x 
        ball.rect.y += speed_y

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
            game_over = True
        
        if ball.rect.x > win_width:
            finish= True
            window.blit(lose2,(200,200))
            game_over = True

        player1.reset()
        player2.reset()
        ball.reset()
    clock
    display.update()
 
  