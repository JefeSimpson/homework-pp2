import pygame 
import sys
import random
import time

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COIN_NUM = 0

#constumization and constants
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game over", True, (255, 255, 255))
background = pygame.image.load("images\\AnimatedStreet.png")
SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
SURF.fill((255, 255, 255))
pygame.display.set_caption("street racer")
clock = pygame.time.Clock()
pygame.mixer.Sound("sounds\\background.wav").play()

#creating Enemy with init and move func
class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load("images\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(85, SCREEN_WIDTH - 85), 0)
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600: 
            self.rect.top = 0
            self.rect.center = (random.randint(85, SCREEN_WIDTH -85), 0)
    '''
    def draw(self, surf):
        surf.blit(self.image, self.rect) 
    '''
#creating Player with init and move func using sprites
class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load("images\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self): 
        pressed_keys = pygame.key.get_pressed() 
        if self.rect.left > 50: 
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH - 50: 
            if pressed_keys[pygame.K_RIGHT]: 
                self.rect.move_ip(5, 0)
        if self.rect.top > 0: 
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT: 
            if pressed_keys[pygame.K_DOWN]: 
                self.rect.move_ip(0, 5)
    '''
    def draw(self, surf): 
        surf.blit(self.image, self.rect)
    '''
#creating Coin with init and spawn randomer, also using sprite
class Coin(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images\\Coin.png"), (2895//60.3, 2913//60.7))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(85, SCREEN_WIDTH -85), random.randint(10, SCREEN_HEIGHT - 10))
    def spawn(self): 
        global COIN_NUM
        COIN_NUM += 1
        self.rect.center = (random.randint(85, SCREEN_WIDTH -85), random.randint(10, SCREEN_HEIGHT - 10))


P1 = Player()
E1 = Enemy()
C1 = Coin()
#adding them after creating
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies.add(E1)
coins.add(C1)
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#game func
while True: 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
    #background image, coin_score surface(blit) 
    SURF.blit(background, (0, 0))
    coin_num = font_small.render(str(COIN_NUM), True, (255, 255, 255))
    SURF.blit(coin_num, (SCREEN_WIDTH - 30, 10))
    #draw func
    for entity in all_sprites: 
        SURF.blit(entity.image, entity.rect)
        if not isinstance(entity, Coin): 
            entity.move()
    #we use sprite func to check collision, and then end the game
    if pygame.sprite.spritecollideany(P1, enemies): 
        pygame.mixer.Sound("sounds\\crash.wav").play()
        time.sleep(0.5)

        SURF.fill((255, 0, 0))
        SURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites: 
            entity.kill()
        time.sleep(4)
        pygame.quit()
        sys.exit()
    #collision for the coin
    if pygame.sprite.spritecollideany(P1, coins): 
        SPEED += 1
        C1.spawn()
    pygame.display.update()
    clock.tick(60)
    
    

