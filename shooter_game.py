from pygame import *
from random import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y +=  self.speed
lost = 0
number = 0 
class Enemy(GameSprite):
    def update(self):
        global lost
        global number
        if number == 10 or lost == 5:
            self.kill()
        self.rect.y += self.speed 
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
class bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed


font.init()
font1 = font.Font(None, 36)



win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
monsters = sprite.Group()
bullets = sprite.Group()

player = Player('rocket.png',5, win_height-80, 10)
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
clock = time.Clock()
FPS = 60
game = True
clock = time.Clock()
finish = False 
wait = 120
wait2 = 120

win = font1.render('YOU WIN', True, (250, 215, 0)) 
wind = font1.render('YOU LOSE', True, (250, 215, 0))

while game:
    window.blit(background,(0, 0))
    text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
    text_lose1 = font1.render('счет: ' + str(number), 1, (255, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                bullets.add(bullet('bullet.png',player.rect.x,player.rect.y, 10))
    if finish != True and wait2 != 0:
        if wait == 0:
            wait = 120
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
            monsters.add(Enemy('ufo.png',randint(5,420),-80, randint(1,3)))
           
                
        
        else:
            wait -= 1
        
        window.blit(text_lose,(0, 0))
        window.blit(text_lose1,(0, 35))

        player.reset()  
        player.update()
        bullets.draw(window)
        bullets.update()
        monsters.draw(window)
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for a in sprites_list:
            number = number + 1
    if number == 10:
        window.blit(win,(280, 225))
        finish = True
        for a in sprites_list1:
            number = number + 1
    if number == 3:
        window.blit(wind,(280, 225))
        finish = True
        if wait2 == 0:
            wait2 = 360
            lost = 0
            total = 0
            number = 0
        else:
            wait2 -= 1

    if lost == 5:
        window.blit(wind,(280, 225))
        finish = True
        if wait2 == 0:
            wait2 = 360
            lost = 0
            total = 0
            lost = 0
            finish = False
        else:
            wait2 -= 1
    monsters.update()
    display.update()
    clock.tick(FPS)