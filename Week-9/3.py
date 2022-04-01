import pygame

pygame.init()
width = 640
height = 480
win = pygame.display.set_mode((width, height))
done = False
radius = 25
speed = 20 
x = 320
y = 240
red = (255, 0, 0)
clock = pygame.time.Clock()

while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y >= radius:
        y -= speed
    elif pressed[pygame.K_DOWN] and y <= height - radius: 
        y += speed
    elif pressed[pygame.K_LEFT] and x >= radius: 
        x -= speed
    elif pressed[pygame.K_RIGHT] and x <= width - radius: 
        x += speed

    win.fill((0, 0, 0))
    pygame.draw.circle(win, red, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)