import pygame
import time

pygame.init()
pygame.mixer.music.load("sound/sound1.mp3")
pygame.mixer.music.play()

# Attendre que la musique se termine
while pygame.mixer.music.get_busy():
    time.sleep(1)

pygame.quit()
