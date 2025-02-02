import pygame

pygame.mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)

pygame.mixer.init()

pygame.mixer.music.load("audiobook.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass

print("Done playing music")
