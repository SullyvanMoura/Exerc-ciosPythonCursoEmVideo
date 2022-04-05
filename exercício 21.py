import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('oioio.mp3')
pygame.mixer.music.play()
print('Hello :)')
pygame.event.wait()
