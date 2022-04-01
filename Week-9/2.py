import pygame
import os

pygame.init()
path = "C:\\Users\\Ата\\PP2-projects\\homework-pp2-master\\Week-9\\sounds"
os.chdir(path)
songs = ["song-1.mp3", "song-2.mp3", "song-3.mp3"]
width = 640
height = 480
win = pygame.display.set_mode((width, height))
song_order = 0
pygame.mixer.music.load(songs[song_order])
pygame.mixer.music.play(0)
done = False
FPS = 60
clock = pygame.time.Clock()

flPause = False
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                if flPause: 
                    pygame.mixer.music.unpause()
                    flPause = not flPause
            if event.key == pygame.K_DOWN: 
                if not flPause:
                    pygame.mixer.music.pause()
                    flPause = not flPause
            if event.key == pygame.K_RIGHT: 
                if song_order + 1 != len(songs): 
                    song_order += 1
                else: 
                    song_order = 0
                pygame.mixer.music.load(songs[song_order])
                pygame.mixer.music.play(0)
            if event.key == pygame.K_LEFT: 
                if song_order != 0: 
                    song_order -= 1
                else:
                    song_order = len(songs) - 1
                pygame.mixer.music.load(songs[song_order])
                pygame.mixer.music.play(0)

    clock.tick(FPS)