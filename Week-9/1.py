import pygame
import datetime
import os
path = path = "C:\\Users\\Ата\\PP2-projects\\homework-pp2-master\\Week-9\\images"
os.chdir(path)
pygame.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))
center = width//2, height//2
clock = pygame.time.Clock()
mickey = pygame.transform.scale(pygame.image.load("mickey-mouse.jpg"), (1280*5//8, 1280*5//8))
left = pygame.transform.scale(pygame.image.load("left.png"), (770//2, 230//2))
right = pygame.transform.scale(pygame.image.load("right.png"), (594//2, 322//2))
done = False

white = (255, 255, 255)

def move(image, pos, ang):
    image_rect = image.get_rect(topleft = (center[0] - pos[0], center[1] - pos[1]))
    offset_center_to_pivot = pygame.math.Vector2(center) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(ang)
    rotated_image_center = (center[0] - rotated_offset.x, center[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -ang)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    win.blit(rotated_image, rotated_image_rect)

while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True  
    win.blit(mickey, (0, 0))
    timenow = datetime.datetime.now()
    second = timenow.second
    minute = timenow.minute
    ang = (minute + second / 60) * (360 / 60)
    move(right, (right.get_width() / 2 + 110, right.get_height() / 2 + 75), ang + 75)
    ang = (360 / 60) * second
    move(left, (left.get_width() / 2 - 145, left.get_height() / 2), ang - 87)
    pygame.display.flip()