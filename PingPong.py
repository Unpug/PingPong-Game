from pygame import *

w = 600
h = 500
fps = 60
clock = time.Clock()
window = display.set_mode((w,h))
display.set_caption("PingPong")
bg = (94, 94, 94)
window.fill(bg)

class GameSprite(sprite.Sprite):
   #Class Constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

#Racket
class Racket(GameSprite):
    def update(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < h - 80:
           self.rect.y += self.speed

class Racket2(GameSprite):
    def update(self):
       keys = key.get_pressed()
       if keys[K_p] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_l] and self.rect.y < h - 80:
           self.rect.y += self.speed

font.init()
font = font.Font(None, 80)
win1 = font.render("Player One Wins!",True,(138, 138, 138))
win2 = font.render("Player Two Wins!",True,(138, 138, 138))

racket = Racket("Racket.png",10,200,50,70,5)
racket2 = Racket2("Racket.png",530,200,50,70,5)
ball = GameSprite("Ball.png",200,200,40,40,5)
speed_x = 3
speed_y = 3

finish = False
game = True
while game:

   if finish == False:
      window.fill(bg)
      ball.rect.x += speed_x
      ball.rect.y += speed_y

      if ball.rect.x < 0:
         finish = True
         window.blit(win2,(70,200))
      if ball.rect.x > 550:
         finish = True
         window.blit(win1,(70,200))

      if ball.rect.y > h-50 or ball.rect.y < 0:
         speed_y *= -1
      if ball.rect.x > w-50 or ball.rect.x < 0:
         speed_x *= -1

      if sprite.collide_rect(ball, racket) or sprite.collide_rect(ball, racket2):
         speed_x *= -1

      racket.update()
      racket2.update()
      ball.reset()
      racket.reset()
      racket2.reset() 

   for e in event.get():
      if e.type == QUIT:
         game = False
   
   display.update()
   clock.tick(fps)